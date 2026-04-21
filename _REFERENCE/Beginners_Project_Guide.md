# A Beginner's Guide to Planning Robust, Secure, Reliable, and Scalable Projects

## And keeping `main` independent of `develop`, always.

---

## Chapter 1 — Core Definitions (plain English)

### Robust
"Doesn't break in surprising ways." Handles bad input, slow networks, partial failures, odd data gracefully.

### Secure
"An attacker can't trivially harm users or the system." Data is confidential, integrity preserved, access controlled.

### Reliable
"Works when users need it." High availability, recovers fast from failures, doesn't lose data.

### Scalable
"Can handle 10x load without rewriting." Cost grows sub-linearly with traffic.

These are **non-functional requirements**. They matter as much as features.

---

## Chapter 2 — The Planning Phases

### 2.1 Frame the Problem
Before writing code, write a 1-page document:
- **Who** uses this?
- **What** job are they hiring it to do?
- **Why** now?
- **Success metrics**: e.g. "500 ms p95 latency, 99.9% uptime, 10k concurrent users."
- **Non-goals**: things you explicitly will NOT build.

If you can't write this in 1 page, you don't understand the problem yet.

### 2.2 Capture Requirements
Two lists:
1. **Functional** — user stories. "As a user, I can...".
2. **Non-functional** — SLIs/SLOs:
   - Latency (p50/p95/p99).
   - Availability (99.9% = 8.76 hr downtime/year).
   - Durability (data loss tolerance).
   - Throughput (requests/sec).
   - Security (compliance: SOC2, GDPR, HIPAA?).
   - Cost envelope (monthly budget).

### 2.3 Back-of-Envelope Estimates
- Users × sessions × actions = QPS.
- Storage = items × size × retention.
- Bandwidth = QPS × payload.
- If numbers look scary, design changes before you code.

### 2.4 Draft Architecture
Boxes + arrows. Typical layers:
1. Client (web / mobile / API consumer).
2. Edge (CDN, WAF, rate limiter).
3. API Gateway.
4. Services (monolith or microservices).
5. Data (SQL / NoSQL / cache / queue / object store).
6. Background workers.
7. Observability stack (logs, metrics, traces).

### 2.5 Choose the Stack
Favor **boring, popular tech**. Postgres beats exotic DBs for 95% of projects. Python/Node/Go beats niche languages for hiring + docs.

Rules:
- 1 primary database (default: Postgres).
- 1 cache (default: Redis).
- 1 queue (default: SQS / RabbitMQ / Redis streams).
- 1 object store (default: S3-compatible).
- 1 orchestrator (default: Kubernetes OR managed platform).

### 2.6 Plan the Repository
- Monorepo vs polyrepo — start **monorepo** unless you have reason not to.
- Directory layout: `app/`, `infra/`, `docs/`, `tests/`, `.github/workflows/`.
- README must answer: what is it, how to run it, how to test it, how to deploy.

### 2.7 Plan the Branch Strategy (see Chapter 3).

### 2.8 Set Up CI / CD Before First Feature
Pipeline from day 1:
- lint + format check
- unit tests
- type check
- security scan (secrets, deps)
- build artifact
- deploy to staging
- smoke tests
- gated promotion to prod

### 2.9 Observability From Day 1
Add logs, metrics, traces before you need them. Dashboards + alerts follow.

### 2.10 Define SLOs + Error Budgets
If target availability = 99.9%, you have 43 min/month error budget. When budget is near-zero, freeze risky changes.

---

## Chapter 3 — Branching: `main` Must NEVER Depend on `develop`

This is the core question. Answer: **keep `main` fully self-contained at every commit.** Read the rules below; apply all.

### 3.1 The Problem Stated
"main depends on develop" means `main` has code that references or is only valid when some change on `develop` is also applied. That is a ticking bomb — a hotfix on `main` will break because the missing piece sits on `develop`.

### 3.2 Pick a Workflow

#### Option A — Trunk-Based Development (recommended for most teams)
- One long-lived branch: `main`.
- All work in short-lived feature branches (< 2 days).
- Merge frequently to `main`.
- Incomplete features hidden behind **feature flags**.
- Releases = tags on `main`.
- **No `develop` branch exists.**

If `develop` doesn't exist, `main` can't depend on it. Simplest possible answer.

#### Option B — GitFlow (only if you truly need it)
Classic: `main` (prod) ← `release/*` ← `develop` ← `feature/*`.
In this model, follow the strict rules below or you WILL end up with dependencies.

### 3.3 Hard Rules to Guarantee Independence

Apply these **all** — each plugs a common leak:

1. **`main` is protected.** No direct pushes. Only PRs from:
   - `release/*` (in GitFlow)
   - `hotfix/*` (short-lived, branched from `main`)
   - Approved feature branches (in trunk-based)

2. **Every commit on `main` must be deployable on its own.** If you can't check out that commit and build+test+deploy it cleanly, it's broken.

3. **Required CI checks on `main`:**
   - All tests pass.
   - Lint + type check pass.
   - Security scan pass.
   - Build + artifact produced.
   - Docker image builds.
   - Integration tests pass against a fresh ephemeral env (not `develop`'s env).

4. **No cherry-picks FROM `develop` TO `main`.** A hotfix is coded on a branch cut from `main`, merged to `main`, then merged back to `develop`. Never the other way.

5. **Hotfix branches are cut from `main`, not `develop`:**
   ```
   git checkout main
   git checkout -b hotfix/bug-123
   # fix, test
   # PR -> main (merge), then PR -> develop (merge)
   ```

6. **Release branches merge INTO `main`, and that merge is the final word.** Once a release lands on `main` and is tagged, you do not touch `develop` to "also apply" something to fix `main`. If something's missing, you cut a `hotfix/*` from `main`.

7. **Tag every release on `main` with a semantic version.** `v1.4.2`. This makes rollback trivial: `kubectl rollout undo` or redeploy `v1.4.1` image.

8. **Artifacts are built from `main` commits, not `develop`.** Prod images are only ever built from tagged `main` commits. Never push an image built from `develop` to prod.

9. **Feature flags for incomplete code.** Code can be on `main` while turned off. This lets you merge often without shipping broken features.

10. **Config and secrets are per-environment, not per-branch.** `main` + prod-config = prod. `main` + staging-config = staging. Never tie code branch to environment config.

11. **Database migrations must be backward-compatible.** A `main` deploy must work with the *current* DB schema AND the next. Rule: expand → migrate → contract. Never ship a single PR that renames/drops a column and the code using it.

12. **Dependencies are pinned and vendored if critical.** A fresh checkout of `main` from 6 months later must still build. Lock files (`package-lock.json`, `poetry.lock`, `Cargo.lock`, `go.sum`) committed.

13. **CI pipeline defined in the repo (`.github/workflows/`).** Don't rely on external state or branch configs only existing on `develop`.

14. **Required CODEOWNERS review.** At least one reviewer per area.

15. **No `git merge develop` on `main` during a hotfix.** Ever. You pull develop in only through the normal release channel.

### 3.4 Concrete GitHub Branch Protection (tick every box)

On `main` settings:
- [x] Require pull request before merging.
- [x] Require approvals (≥ 1).
- [x] Dismiss stale reviews on new commits.
- [x] Require review from Code Owners.
- [x] Require status checks to pass (list them all).
- [x] Require branches to be up to date before merging.
- [x] Require linear history (rebase / squash merges, no merge commits).
- [x] Require signed commits.
- [x] Require conversation resolution.
- [x] Do not allow bypassing the above — include administrators.
- [x] Restrict who can push / force-push: nobody.
- [x] Lock branch against deletion.

### 3.5 The Self-Containment Test
At any point, run:
```bash
git checkout main
git clean -fdx
# install deps, build, test, run
```
If anything fails, `main` is not self-contained. Fix that before anything else.

### 3.6 Symptoms That Main Depends on Develop (red flags)
- Hotfix PR CI passes only after "also merging" some develop commit.
- Engineers say "you need to cherry-pick that from develop".
- Builds fail when `develop` is behind `main` on shared libs.
- Environment vars used in `main` are defined only on develop-tagged artifacts.
- README or migration steps live only on `develop`.

Any one of these → independence is broken. Go fix it.

---

## Chapter 4 — Robustness at Every Step

| Step | Apply |
|------|-------|
| **Requirements** | Ask "what could go wrong?" for each story. |
| **Design** | Identify failure domains (instance / AZ / region). Design to survive the worst tolerable one. |
| **Code** | Validate inputs at boundaries. Fail closed on errors. Return typed errors, not nulls. |
| **Timeouts** | Every network call has one. Default: 5s. Never infinite. |
| **Retries** | Exponential backoff + jitter. Cap attempts (3-5). |
| **Circuit breakers** | Open after N failures. Half-open to test recovery. |
| **Idempotency** | Mutating endpoints accept idempotency keys. |
| **Graceful degradation** | Feature off > site off. Cached data > no data. |
| **Testing** | Unit + integration + contract + chaos. |
| **Runtime** | Health checks, readiness vs liveness. Graceful shutdown (SIGTERM → drain → exit). |

---

## Chapter 5 — Security at Every Step

### 5.1 Shift Left
Security during design, not after launch.

### 5.2 Threat Model (STRIDE)
For each component ask about:
- **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege.

### 5.3 The 10 Beginner Musts
1. **Never commit secrets.** `.env` in `.gitignore`. Use Vault / AWS Secrets Manager / GitHub Secrets.
2. **HTTPS everywhere.** Redirect HTTP → HTTPS. HSTS header.
3. **Authenticated by default.** Deny unless explicitly public.
4. **Authorization on every endpoint.** Check role + resource ownership.
5. **Validate input at the boundary.** Trust no client.
6. **Parameterize queries.** Never string-concat SQL.
7. **Escape output.** XSS prevention. Use framework defaults.
8. **Rate limit.** Per user, per IP, per endpoint.
9. **Patch deps weekly.** Dependabot / Renovate.
10. **Log auth events, don't log secrets.**

### 5.4 CI Security Gates (automate)
- Secret scan (gitleaks).
- Dep scan (Snyk / Trivy / Dependabot).
- SAST (Semgrep, CodeQL).
- IaC scan (Checkov, tfsec).
- Container scan (Trivy, Grype).
- License scan.

### 5.5 Data
- Encrypt at rest (disk / DB feature).
- Encrypt in transit (TLS).
- Minimize PII collected.
- Set retention policies; delete on schedule.
- Backup encrypted + tested (restore drill every quarter).

### 5.6 Identity + Access
- MFA for all humans.
- Least privilege — no `*` wildcards.
- Short-lived credentials (OIDC federation beats static keys).
- Audit log everything.

---

## Chapter 6 — Reliability at Every Step

### 6.1 Redundancy
- Multiple instances behind a load balancer.
- Multi-AZ for DB (managed DB handles this).
- Multi-region for critical paths (active-passive first).

### 6.2 Statelessness
App servers stateless → replace any time. State lives in DB / cache / object store.

### 6.3 Backups + DR
- Automated backups (daily + hourly).
- Define **RPO** (data loss tolerance) and **RTO** (time to restore).
- Test restore. An untested backup is an assumption.

### 6.4 Deployment
- **Blue-green** or **canary** — never big-bang.
- Automated rollback (on elevated error rate / latency).
- Feature flags to kill broken features fast.

### 6.5 Observability
Three pillars:
- **Logs** — structured JSON, correlation id.
- **Metrics** — RED (Rate, Errors, Duration) + USE (Utilization, Saturation, Errors).
- **Traces** — OpenTelemetry, distributed spans.

Set alerts on SLO burn rate, not raw metrics.

### 6.6 On-call + Postmortems
- Rotation, runbooks, pager threshold.
- Blameless postmortems. Action items tracked to closure.

---

## Chapter 7 — Scalability at Every Step

### 7.1 Design for Horizontal Scale First
Prefer many small instances over one big one. Stateless apps + shared state tier scales best.

### 7.2 Data Layer
- Read replicas first.
- Cache second (Redis / CDN).
- Sharding third (painful; delay as long as possible).
- Consider columnar warehouse for analytics (separate from OLTP).

### 7.3 Async by Default
For anything > 100ms, push to queue. Users don't wait on emails, reports, ML inference, etc.

### 7.4 CDN + Edge
Static assets + cacheable API responses → CDN. Reduces origin load ~10x.

### 7.5 Auto-scaling
- Horizontal Pod Autoscaler (K8s) on CPU / QPS / custom metric.
- Cluster autoscaler for infra.
- Pre-warm for known spikes.

### 7.6 Cost Control (FinOps)
- Tag every resource.
- Budgets + alerts.
- Right-size weekly.
- Use spot/preemptible for batch.
- Reserved / savings plans when usage is stable.

### 7.7 Measure Before You Optimize
Profile in production-like load. Amdahl's law: only the slow part matters.

---

## Chapter 8 — Step-by-Step Project Checklist

### Before first line of code
- [ ] 1-page problem doc.
- [ ] Functional + non-functional requirements.
- [ ] Architecture diagram (boxes + arrows).
- [ ] Stack chosen; tradeoffs written down.
- [ ] Threat model done.

### Day 1 of coding
- [ ] Repo created with README, LICENSE, `.gitignore`, `.editorconfig`.
- [ ] Linter + formatter configured.
- [ ] Branch protection on `main` (see Chapter 3.4).
- [ ] CI pipeline runs on every PR.
- [ ] Pre-commit hooks.
- [ ] Secret management chosen; no secrets in code.
- [ ] Logging + metrics scaffolding.
- [ ] Dockerfile + dev compose file.

### Every PR
- [ ] Small (< 400 lines diff).
- [ ] Tests added.
- [ ] No secrets added.
- [ ] CI green.
- [ ] Reviewed by owner.
- [ ] Linked to ticket.

### Before staging deploy
- [ ] Migration plan (forward + backward compatible).
- [ ] Rollback plan documented.
- [ ] Feature flag wired (if risky).
- [ ] Load test result captured.

### Before prod deploy
- [ ] Staging smoke + e2e pass.
- [ ] Error-budget not exhausted.
- [ ] On-call aware.
- [ ] Monitoring + alerts verified.

### Post-deploy
- [ ] Watch dashboards for 30 min.
- [ ] Gradual canary → full.
- [ ] Postmortem if any incident.

---

## Chapter 9 — Rules to Live By

1. **If it's not in version control, it doesn't exist.**
2. **If it's not tested, it's broken.**
3. **If it's not monitored, it's already on fire.**
4. **If you didn't automate it, you'll forget it.**
5. **If it can't be rolled back in < 5 min, it shouldn't be deployed.**
6. **If `main` isn't always deployable, nothing else matters.**
7. **Boring tech is resume-boring, not career-boring.**
8. **Two is one, one is none** (redundancy).
9. **Premature optimization is the root of most evil.**
10. **Documentation is part of the deliverable.**

---

## Appendix A — Branch Protection as Code (GitHub)

```yaml
# .github/settings.yml (requires Probot: Settings app)
branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 1
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
      required_status_checks:
        strict: true
        contexts:
          - ci/lint
          - ci/typecheck
          - ci/test
          - ci/security-scan
          - ci/build
      enforce_admins: true
      required_linear_history: true
      required_signatures: true
      restrictions: null
      allow_force_pushes: false
      allow_deletions: false
```

## Appendix B — Starter CI Pipeline (GitHub Actions)

```yaml
name: CI
on: [push, pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements-dev.txt
      - run: ruff check .
      - run: mypy .
      - run: pytest --cov --cov-fail-under=80
      - uses: gitleaks/gitleaks-action@v2
      - uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          severity: CRITICAL,HIGH
```

## Appendix C — Hotfix Workflow (diagram)

```
main (v1.4.1) ──┬──────────────────┬── tag v1.4.2
                │                  │
                └─ hotfix/bug-123 ─┘
                         │
                         └── also merge into → develop
```

## Appendix D — Further Reading

- *The Phoenix Project* — Kim, Behr, Spafford.
- *Accelerate* — Forsgren, Humble, Kim.
- *Site Reliability Engineering* — Google.
- *Designing Data-Intensive Applications* — Kleppmann.
- OWASP Top 10 — owasp.org.
- 12-Factor App — 12factor.net.
- Trunk-Based Development — trunkbaseddevelopment.com.

---

*End of guide.*
