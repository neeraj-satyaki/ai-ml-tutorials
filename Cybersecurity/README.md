# Cybersecurity — Full Curriculum + Case Studies

Broader than `NetworkSecurity/`. Covers offensive, defensive, forensics, malware, crypto, cloud, IoT, Web3, AI/ML security, compliance.

## Fundamentals
CIA triad, AAA (authn/authz/accounting), risk mgmt. Threat models: STRIDE, PASTA, LINDDUN. Attack surface, defense-in-depth, least privilege, secure-by-design, Zero Trust. Chain of custody. Policies + governance.

## Cryptography
Symmetric (AES, ChaCha), asymmetric (RSA, ECC, EdDSA), hashes (SHA-2/3, BLAKE), HMAC, KDFs (PBKDF2, scrypt, Argon2). Digital signatures. PKI (X.509, chain, CRL/OCSP, Certificate Transparency). CSPRNG. TLS handshake + PFS. Post-quantum (Kyber, Dilithium, SPHINCS+). Homomorphic (BFV, CKKS, TFHE). MPC + secret sharing. ZKP (SNARK, STARK, Bulletproofs). Crypto agility.

## Application Security
OWASP Top 10 (2021) + API Top 10. Secure SDLC, NIST SSDF. SAST + DAST + IAST. SCA + dep scans. Fuzzing (AFL, libFuzzer). Secrets detection (gitleaks, trufflehog). SSRF, deserialization, TOCTOU, business logic flaws. Supply-chain security — lockfiles, SBOM, SLSA, Sigstore/cosign.

## Web Security
Same-origin + CORS. CSP, Trusted Types, SRI. Cookies (Secure, HttpOnly, SameSite). Clickjacking. MIME sniffing. Cache poisoning. HTTP request smuggling/desync. XS-Leaks. Session fixation. OAuth PKCE, JWT pitfalls (alg=none, key confusion). GraphQL intro attacks.

## Network Security (deep)
Port scanning, ARP poison, DNS spoofing, BGP hijack, VLAN hopping. Firewalls (stateful/NGFW), WAFs, IDS/IPS (Snort, Suricata, Zeek), DDoS mitigation, rate limiting, bot management, ZTNA/SASE/BeyondCorp, NAC, SD-WAN security.

## Cloud Security
IAM deep dive (AWS SCP/OU, GCP VPC-SC, Azure Conditional Access). Misconfigs (open S3). CIS benchmarks. CSPM (Prisma, Wiz, Orca), CWPP, CIEM. KMS/CMEK/BYOK. Container sec. Kubernetes CIS bench + Pod Security Admission. Admission controllers (OPA, Kyverno). GitOps security. Image scanning + signing.

## IAM / Identity
JML lifecycle, SSO (SAML/OIDC), MFA (TOTP/HOTP/hardware keys/WebAuthn/PassKeys), passwordless, PAM + JIT, service accounts, workload identity (SPIFFE/SPIRE), access reviews/certifications.

## Endpoint Security
NGAV/EDR/XDR, HIDS (OSSEC, Wazuh), patching, USB/device control, disk encryption (BitLocker/LUKS/FileVault), MDM/UEM (Intune, Jamf), browser isolation, TPM/secure boot/measured boot, OS hardening.

## Malware Analysis
Static: PE/ELF/Mach-O. Dynamic: sandboxing (Cuckoo, ANY.RUN, Joe). RE: IDA, Ghidra, radare2/Cutter, Binja. Debuggers: x64dbg, WinDbg, gdb. Unpacking (UPX), control-flow obfuscation. IOC extraction (YARA, Sigma). Family clustering (CAPE).

## Digital Forensics
DFIR process. Chain of custody. Disk imaging (dd, FTK Imager). Memory forensics (Volatility). Timeline (Plaso, Timesketch). Artifacts (Registry, Event Logs, prefetch, MFT). Mac/Linux artifacts. Mobile (Cellebrite, MSAB). Network forensics (Zeek, Wireshark). Cloud forensics. Threat intel (MITRE ATT&CK).

## Offensive Security (authorized)
Recon/OSINT (Shodan, Maltego). Enum + scanning. Vuln assessment (Nessus, OpenVAS). Exploit dev — BOF, heap, format string, ROP, kernel. Web exploitation (Burp, sqlmap, BeEF). Wireless (Aircrack, Wifite). Mobile (Frida, Objection, MobSF). Cloud pentest. AD pentest (Bloodhound, Rubeus, Mimikatz). Social engineering (GoPhish, Evilginx). C2 frameworks. Evasion. Purple team. Certs: OSCP, OSCE, CRTE, CRTP, PNPT. Bug bounty workflows.

## Defensive / Blue Team
SOC tiers. Detection engineering + Sigma rules. SPL (Splunk), KQL (Elastic). MITRE ATT&CK coverage. Threat hunting. Deception. SOAR automation (Tines, Torq, XSOAR). IR (NIST/SANS). Tabletop + purple team exercises. ATT&CK evaluations.

## Threat Intel (CTI)
Lifecycle (plan → collect → process → analyze → disseminate). Pyramid of Pain. Diamond Model. Lockheed Kill Chain + Unified Kill Chain. STIX/TAXII IOC sharing. TTP mapping.

## Compliance / Frameworks
NIST CSF 2.0, NIST 800-53/171, ISO 27001/27002, SOC 2 Type I/II, PCI-DSS 4.0, HIPAA, GDPR, CCPA/CPRA, FedRAMP, CMMC, COBIT, FAIR, CIS Controls v8.

## Privacy Engineering
Privacy by Design (7 principles), data minimization, pseudonymization/anonymization, differential privacy, tokenization, DSAR handling, right-to-erasure, ROPA, DPIA/PIA, data residency/sovereignty.

## OT / ICS / SCADA
ICS (PLC, DCS, HMI). Protocols: Modbus, DNP3, IEC 61850. Purdue model. Air-gap myths. Stuxnet learnings. Industroyer/CrashOverride. TRITON/TRISIS. Havex. ICS detection (Dragos, Claroty, Nozomi).

## IoT / Embedded Security
HW attacks: fault injection, side-channel (power/timing), glitching. JTAG/SWD attacks. Bootloader exploits. Secure boot, TEE, TrustZone. Firmware analysis (binwalk, EMBA). BLE/Zigbee/Z-Wave/Thread attacks. Chip-off NAND dump. Protocol fuzzing.

## AI / ML Security
Adversarial examples (FGSM, PGD, CW). Model inversion/extraction. Data poisoning / backdoors. Prompt injection + jailbreaks. Membership inference. DP for ML. Federated learning sec (Secure Agg, Krum). ML supply chain. Red-teaming LLMs. MITRE ATLAS. AI-BOM.

## Blockchain / Web3 Security
Smart contract bugs: reentrancy, integer overflow, access control, oracle manipulation, front-running (MEV). Famous incidents: The DAO, Parity, Harmony, Ronin, Wormhole. Tooling: Slither, Mythril, Echidna, Foundry/Forge. Audit methodology. Cross-chain bridge risks. Wallet sec (MPC). Flash-loan attacks. Governance attacks (Poly Network). Custody (HSM, multisig/Safe).

---

## Case Studies (in `CaseStudies_Breaches/`)

| Year | Incident | Key takeaway |
|------|----------|--------------|
| 2010 | Stuxnet | Nation-state ICS/SCADA + zero-days + worm |
| 2014 | Heartbleed | OpenSSL buffer overread; test critical crypto libs |
| 2014 | Sony Pictures | Destructive malware; wiper payload |
| 2015 | OPM | Mass PII theft; slow detection |
| 2015 | Ukraine Power Grid | First public grid takedown (BlackEnergy) |
| 2016 | Mirai | IoT botnet using default creds; massive DDoS |
| 2017 | Equifax | Unpatched Struts → 147M records |
| 2017 | NotPetya | Destructive supply-chain (M.E.Doc) |
| 2017 | WannaCry | EternalBlue + SMBv1 + killswitch |
| 2020 | SolarWinds (SUNBURST) | Supply-chain compromise at build stage |
| 2021 | ProxyLogon (Exchange) | 4 zero-days; mass exploitation |
| 2021 | Colonial Pipeline | Ransomware on IT → OT ops stopped |
| 2021 | Kaseya / REvil | MSP supply chain; thousands of MSPs affected |
| 2021 | Log4Shell | Log4j JNDI RCE; widest-ever vuln |
| 2022 | Okta / LAPSUS$ | Third-party access; simple social eng at scale |
| 2022 | Uber | MFA fatigue + internal creds in scripts |
| 2022-23 | LastPass | Data + encrypted vault breach; long dwell |
| 2023 | MOVEit (Cl0p) | SQLi zero-day → widespread extortion |
| 2023 | MGM/Caesars (Scattered Spider) | Help-desk voice-based social engineering |
| 2024 | Change Healthcare | Ransomware, $22M paid, prolonged outage |
| 2024 | CrowdStrike outage | Faulty kernel driver update → global BSOD |
| 2024 | Snowflake customer breaches | Unprotected accounts w/o MFA + infostealer creds |
| 2024 | XZ Utils backdoor (CVE-2024-3094) | Multi-year social eng against OSS maintainer |
| 2024 | AT&T customer data dump | Cloud DB exposed; 73M records |
| 2024 | Microsoft Midnight Blizzard | Password spray → OAuth abuse → email theft |

---

## Skill ladder
1. **Fundamentals + web + network sec** (0-6 mo).
2. Pick lane: **offensive** (pentest), **defensive** (SOC/DE/IR), **appsec**, **cloud sec**, **IAM**, **GRC**, **research**.
3. Certs (optional but useful): **Sec+** → **CySA+ / Net+ / Linux+ → OSCP or GCIH** → specialize.
4. CTFs: HackTheBox, TryHackMe, Root-Me, picoCTF, CTFtime events.
5. Read reports daily: Mandiant, Google TAG, Microsoft, Unit 42, Volexity, Citizen Lab, Sekoia.
