# Plan — Build JWT auth with key rotation for a public API

> Stateless authentication for a multi-tenant public API. Signs short-lived access tokens with rotating asymmetric keys, exposes JWKS, and revokes via a refresh-token allow-list. Independently scalable from the data plane.

## Non-goals
- Replacing SSO for employees (use Okta/Clerk for that).
- Storing PII inside tokens (claims stay minimal).
- Supporting legacy HS256 clients.

## Open Questions
- Is audience segmentation per-tenant or per-app? Affects `aud` claim design.
- Do we need token binding (RFC 8473) for anti-replay?
- Refresh token rotation strategy: one-shot vs family-tracking?

## Domain: Backend
> **Why:** Token issuance + verification lives in the API tier. Cache / DB are downstream.

### Concept: API Security Layer
> **Why:** Auth must be a single, well-tested middleware — not sprinkled across handlers.

#### Chapter: Token Strategy
> **Why:** Choose stateless JWT vs stateful session first; all downstream rules follow.

##### Topic: JWT (JSON Web Token)
> **Why:** Stateless verification scales; no shared session store per instance.
> **Refs:** `Backend/Auth/JWT_Design_Security/`, `_REFERENCE/When_To_Use.md`

- **Rule:** Use RS256 or EdDSA, never HS256.
  - *Why:* RS256/EdDSA allow public verification → key rotation without distributing secrets to every service.
  - *Enforce:* Reject `alg=HS256` and `alg=none` in the verifier; unit test this.
- **Rule:** Access token TTL ≤ 15 minutes.
  - *Why:* Shorter window limits damage from token theft; refresh compensates for UX.
  - *Enforce:* Policy in token factory + metric alert if `exp−iat > 900s`.
- **Rule:** Include `iss`, `aud`, `sub`, `iat`, `exp`, `jti`. No PII.
  - *Why:* Minimal claims reduce information disclosure if a token leaks.
- **Rule:** Reject tokens outside a ±60s clock skew.
  - *Why:* Tight clock-skew limits replay windows.

#### Chapter: Key Management
> **Why:** Rotation is the single biggest safety lever — most incidents failed at this layer.

##### Topic: JWKS + Rotation
> **Why:** Public JWKS endpoint lets clients pick up new keys without redeploys.
> **Refs:** `Cybersecurity/Cryptography/PKI_X509_CertificateChains/`, `Backend/Auth/Tokens_Refresh_Rotation_RevocationLists/`

- **Rule:** Rotate signing keys at least every 24 hours; keep 3 public keys live.
  - *Why:* Old tokens stay verifiable until expiry; compromised keys stop being used quickly.
  - *Enforce:* Cron rotator + audit log per rotation + alert on age > 36h.
- **Rule:** Private keys live in KMS (AWS/GCP/HSM), never on disk.
  - *Why:* Breach of a pod cannot exfiltrate the signing key.
  - *Enforce:* CI scan for `.pem` files; runtime check that signing goes through KMS.
- **Rule:** Expose `/.well-known/jwks.json` with `Cache-Control: max-age=300`.
  - *Why:* Low cache TTL = fast rotation, still protects against DoS.

##### Topic: Revocation
> **Why:** Stateless JWT cannot be "revoked" — but refresh-token flow can be.
> **Refs:** `Backend/Auth/Tokens_Refresh_Rotation_RevocationLists/`

- **Rule:** Use refresh-token rotation with a persisted allow-list keyed by `jti`.
  - *Why:* Stolen refresh tokens are invalidated the next time the victim refreshes.
  - *Enforce:* Redis store with `EXPIRE` = refresh TTL; alert on reused `jti`.
- **Rule:** Emit a `token_revoked` event on suspicious reuse and invalidate the entire family.
  - *Why:* One leaked refresh → full compromise of that session tree.

### Concept: Transport + Storage
> **Why:** How tokens travel and persist is where most leaks happen.

#### Chapter: Client-side handling
> **Why:** Frontend is the biggest attack surface (XSS, extensions).

##### Topic: Cookie vs `Authorization` header
> **Why:** For browser clients, HttpOnly + SameSite=Strict cookies beat localStorage.
> **Refs:** `Frontend/Security/`, `Cybersecurity/WebSecurity/`

- **Rule:** Browser clients → HttpOnly, Secure, SameSite=Strict cookies.
  - *Why:* JS cannot read the token; XSS cannot exfiltrate.
- **Rule:** Native + service-to-service → Bearer header in `Authorization`.
  - *Why:* No XSS surface; simpler with existing HTTP tooling.
- **Rule:** Never store tokens in `localStorage` or `sessionStorage`.
  - *Why:* Accessible via any XSS.

## Domain: Cybersecurity
> **Why:** Auth is a security feature first. Repo's WebSecurity + Crypto chapters codify the real attack surface.

### Concept: Web Security Hardening
> **Why:** Even a perfect JWT design fails without transport/HTTP protections.

#### Chapter: Protocol-level protections
> **Why:** Wrap auth in defense-in-depth.

##### Topic: TLS + CSP
> **Why:** TLS must be enforced; CSP cuts a class of token-exfil vectors.
> **Refs:** `NetworkSecurity/LayerSecurity/`, `Cybersecurity/WebSecurity/`

- **Rule:** Require TLS 1.2+; HSTS with preload in prod.
  - *Why:* Prevents downgrade + strip attacks on public API.
- **Rule:** Set strict CSP with `script-src 'self' 'nonce-...'`.
  - *Why:* Mitigates XSS that would otherwise steal cookies (even HttpOnly tokens don't survive all vectors).

##### Topic: JWT pitfalls to avoid
> **Why:** Same bug pattern keeps surfacing; lock against it.
> **Refs:** `Cybersecurity/WebSecurity/JWT_Pitfalls_AlgNone_KeyConfusion/`

- **Rule:** Never trust `alg` from the token header; pin to an allow-list.
  - *Why:* `alg=none` and key-confusion (RS→HS) exploits.
- **Rule:** Key ID (`kid`) is a hint only; still verify against configured JWKS.
  - *Why:* Forged `kid` values point to attacker-controlled keys.

## Domain: Ops
> **Why:** Key rotation, token metrics, and incident response live in the operational plane.

### Concept: Observability + IR
> **Why:** Without signal, you won't see the breach until it's on the news.

#### Chapter: Token + key metrics
> **Why:** Auth incidents are detected by anomalies, not exceptions.

##### Topic: SLOs + alarms
> **Why:** Define the signals now; retrofitting is painful.
> **Refs:** `Ops/MLOps/` (monitoring patterns transfer), `SystemDesign/Observability/`

- **Rule:** Metric: `auth.token_issue_failure_ratio` with SLO ≤ 0.1%.
  - *Why:* Spikes = upstream outage (KMS) or abuse.
- **Rule:** Alarm on `jwks.key_age_seconds > 129_600` (36h).
  - *Why:* Catches a stuck rotator before tokens can't verify.
- **Rule:** Alarm on `refresh_token.reuse_detected` count > 0.
  - *Why:* Indicates an active replay attempt.

### Concept: Incident Response
> **Why:** When (not if) a key or token leaks, you need a runbook ready.

#### Chapter: Runbooks
> **Why:** 2 AM decisions should be scripted, not invented.

##### Topic: "Rotate now" procedure
> **Why:** The one procedure ops actually uses; rehearse it.
> **Refs:** `Cybersecurity/DefensiveSecurity_BlueTeam/PlaybooksRunbooks/`

- **Rule:** Emergency rotation must complete in < 5 min end-to-end.
  - *Why:* Window of exposure should be bounded.
  - *Enforce:* Game-day drill every quarter.
- **Rule:** Have a "kill switch" config flag that forces all refresh tokens to expire.
  - *Why:* Nukes all sessions worldwide when you've lost trust in the store.
