# Network Security

Scoped narrower than `Cybersecurity/` — covers network-layer to protocol-level security.

## Layered Security
- **L2**: ARP spoofing, DHCP snooping, port security, 802.1X.
- **L3**: IPsec, GRE, VXLAN, segmentation.
- **L4**: TCP sequence attacks, SYN floods.
- **L7**: TLS (1.2/1.3), HSTS, HPKP (deprecated), DoH/DoT, DNSSEC.

## Perimeter Controls
Firewalls (stateful/NGFW), WAFs, IDS/IPS (Snort, Suricata, Zeek), DDoS mitigation (Cloudflare, Shield), rate limiting, bot management, ZTNA/SASE/BeyondCorp, NAC, secure reverse proxy.

## Authentication + Access
Kerberos, LDAP/AD, OAuth2/OIDC, SAML, WebAuthn/FIDO2, MFA (TOTP/HOTP/hardware), PAM, JIT access, SSH hardening, mTLS, RBAC/ABAC/ReBAC.

## Crypto Protocols
TLS 1.2 / 1.3, IPsec + IKEv2, SSH, WireGuard, OpenVPN, MACsec, QUIC, post-quantum (NIST choices — Kyber, Dilithium, SPHINCS+).

## Monitoring + Response
SIEM, EDR/XDR, NDR, DLP, NetFlow/sFlow, pcap (Wireshark, tcpdump), NIST incident response, threat hunting, honeypots/canary tokens, MITRE ATT&CK.

## Privacy + Compliance
DP, data minimization, tokenization/masking, GDPR/CCPA/HIPAA/PCI-DSS/SOC2/ISO 27001, SBOM/supply-chain, SSDLC.

## Attacks + Defenses
Phishing, ransomware, supply chain (SolarWinds), zero-day triage, lateral movement, exfiltration, MITM, replay, OSINT recon, exploit kits, post-exploitation C2, detection engineering.

See `Cybersecurity/README.md` for broader cyber scope (offensive, malware, forensics, cloud, IoT, web3, case studies).
