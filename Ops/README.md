# Ops — All Disciplines

Every *-Ops: what it means, scope, tools, lifecycle, metrics.

---

## DevOps (`DevOps/`)
Unify Dev + Ops. Continuous delivery of software.

### Scope
Source → Build → Test → Deploy → Operate → Monitor. Infra as code, CI/CD, containerization, orchestration.

### Lifecycle (CALMS + 8-phase)
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → back to Plan.

### Key practices
- **CI/CD** — merge often; automated pipelines. Trunk-based dev.
- **IaC** — Terraform, Pulumi, CloudFormation, Ansible.
- **Containers** — Docker, Podman. Orchestration: Kubernetes, Nomad.
- **GitOps** — declarative state in git, Argo CD / Flux reconciles.
- **Blue-Green, Canary, Rolling** deploys. Feature flags.
- **Observability** — logs, metrics, traces (OpenTelemetry).
- **Incident response** — runbooks, on-call, postmortems.

### Metrics (DORA)
- **Deployment frequency**
- **Lead time for changes**
- **Change failure rate**
- **Mean time to restore (MTTR)**

### Tools
GitHub Actions, GitLab CI, Jenkins, CircleCI, ArgoCD, Flux, Helm, Kustomize, Terraform, Prometheus, Grafana, Datadog.

---

## DevSecOps (`DevSecOps/`)
Security integrated into DevOps pipeline ("shift left").

### Scope
Threat modeling at design; static + dynamic scanning in CI; dependency audits; runtime protection; compliance automation.

### Practices
- **SAST** (Semgrep, CodeQL, SonarQube)
- **DAST** (OWASP ZAP, Burp)
- **SCA / dependency scan** (Snyk, Dependabot, Trivy)
- **IaC scan** (Checkov, tfsec, KICS)
- **Container scan** (Trivy, Grype, Clair)
- **Secret scanning** (gitleaks, trufflehog)
- **SBOM generation** (SPDX, CycloneDX)
- **Policy-as-code** (OPA/Rego, Kyverno)
- **Runtime** (Falco, eBPF probes)

### Metrics
Mean time to remediate (MTTR-sec), vuln leakage to prod, % builds with security gates passing, compliance drift.

---

## GitOps (`GitOps/`)
Git = single source of truth. Operators reconcile actual state with declared.

### Core principles
1. Declarative.
2. Versioned + immutable (git history).
3. Automatically pulled (not pushed).
4. Continuously reconciled.

### Tools
ArgoCD, Flux, Jenkins X, Werf.

### Scenarios
K8s cluster state, app deploys, infra (Crossplane), secrets (Sealed Secrets, External Secrets Operator).

---

## DataOps (`DataOps/`)
Agile + DevOps applied to data pipelines. Reliable, observable, fast data delivery.

### Scope
Ingestion → Transform → Store → Serve → Govern. Schema evolution, data contracts, lineage, quality.

### Key practices
- **Orchestration** — Airflow, Dagster, Prefect, Mage.
- **Transformation** — dbt, Spark, Flink.
- **Data quality** — Great Expectations, Soda, Monte Carlo.
- **Lineage** — OpenLineage, DataHub, Marquez, Atlan.
- **Contracts** — schema + SLO between producers and consumers.
- **Observability** — freshness, volume, schema, distribution drift.
- **Testing** — unit tests on transforms, integration on pipelines.

### Metrics
Data freshness, completeness, accuracy, lineage coverage, pipeline success rate, time-to-detect data incidents.

---

## MLOps (`MLOps/`)
Productionize ML. Bridge data scientists → reliable ML services.

### Lifecycle
Problem framing → data → features → train → validate → deploy → monitor → retrain.

### Key practices
- **Experiment tracking** — MLflow, W&B, Neptune, Comet.
- **Feature store** — Feast, Tecton, Hopsworks.
- **Pipelines** — Kubeflow, Metaflow, ZenML, SageMaker Pipelines, Vertex AI Pipelines.
- **Model registry** — MLflow Registry, W&B Artifacts.
- **Training** — distributed (Ray Train, DeepSpeed, FSDP), auto-ML (AutoGluon, H2O).
- **Serving** — Triton, TorchServe, TFServing, Ray Serve, BentoML, Seldon.
- **CI/CD for ML (CI/CD/CT)** — CT = continuous training.
- **Data + model versioning** — DVC, LakeFS, Git LFS.

### Monitoring
- **Data drift** — KS, PSI, MMD, Evidently.
- **Concept drift** — ADWIN, DDM.
- **Performance** — live labels vs predictions.
- **Service** — latency, QPS, errors.

### Levels (Google)
- Level 0: manual.
- Level 1: automated pipeline.
- Level 2: full CI/CD/CT.

### Metrics
Time to production, rollback rate, model staleness, drift-detection latency, feature backfill cost.

---

## ModelOps (`ModelOps/`)
Broader than MLOps — *all* analytical models: ML, rule engines, optimization, simulation, decision models. Governance + lifecycle at enterprise scale.

### Scope
Model inventory, risk tiers, approval workflows, documentation (model cards), monitoring, retirement.

### Key practices
- **Model cards** (Mitchell et al.), **data sheets for datasets** (Gebru et al.)
- Challenger-champion testing.
- SR 11-7 / model risk management (banking).
- Approval gates by risk tier.

### Tools
Domino, DataRobot MLOps, IBM Cloud Pak for Data, Modzy.

---

## LLMOps (`LLMOps/`)
MLOps for foundation / large language models. Distinct because: inference is the cost, prompts are code, data is streams of text.

### Scope
Prompt engineering → fine-tuning/adapter training → evaluation → serving → monitoring → iterative improvement.

### Stack
- **Prompt management** — LangSmith, Langfuse, PromptLayer, Weave.
- **Fine-tuning** — LoRA/QLoRA, SFT, DPO/GRPO (TRL, unsloth, Axolotl).
- **RAG infra** — vector DB (Pinecone, Weaviate, Milvus, pgvector) + retriever + reranker.
- **Evaluation** — ground truth, LLM-as-judge, human eval, arena-style. Tools: Ragas, DeepEval, TruLens, Braintrust, PromptFoo.
- **Serving** — vLLM, SGLang, TGI, TensorRT-LLM, Triton. Continuous batching, KV-cache reuse, speculative decoding.
- **Observability** — trace every prompt/response/tool call. Token counts, latency, cost, quality drift.
- **Guardrails** — NVIDIA NeMo Guardrails, Guardrails AI, Llama Guard, jailbreak + PII detection.
- **Cost management** — prompt caching (Anthropic/OpenAI), router (small→big model cascade), quantization.

### Metrics
Token $/request, latency p50/p95, task success rate, hallucination rate, toxicity rate, prompt injection rate, retrieval hit@k, response consistency.

---

## AIOps (`AIOps/`)
AI applied to IT operations. NOT "ops for AI" — that's MLOps/LLMOps.

### Scope
Ingest telemetry (logs, metrics, traces, tickets, changes) → correlate → detect anomalies → predict incidents → automate remediation.

### Use cases
- **Anomaly detection** in metrics (Prophet, Isolation Forest, Robust Random Cut Forest).
- **Log clustering** (Drain, LogBERT).
- **Alert correlation / noise reduction** (Moogsoft, BigPanda).
- **Root-cause analysis** via causal graphs / topology.
- **Predictive capacity / failure** — disk failure prediction, autoscaling.
- **ChatOps / agent-driven remediation**.

### Tools
Dynatrace Davis, Splunk ITSI, Datadog Watchdog, New Relic AIOps, PagerDuty Incident Response, IBM Watson AIOps, Moogsoft, BigPanda.

### Metrics
Mean time to detect (MTTD), alert volume reduction, false-positive rate, auto-remediation success, noise-to-signal ratio.

---

## CVOps (`CVOps/`)
MLOps specialized for computer vision.

### Challenges unique to CV
- Huge image/video datasets — storage, transfer, labeling cost.
- Labeling tools + workflow (CVAT, Label Studio, Labelbox, Roboflow, Supervisely).
- Data augmentation pipelines (Albumentations, imgaug).
- Active learning loops — uncertainty sampling on unlabeled pool.
- Edge deployment — quantized + pruned + TensorRT / CoreML / TFLite / ONNX Runtime.
- Video streams — continuous inference at FPS budgets.
- Drift detection on image distributions (embedding drift).
- Synthetic data / sim-to-real (Unity Perception, NVIDIA Omniverse).
- Annotation QA — inter-annotator agreement (Cohen's κ, Fleiss' κ).

### Stack
Roboflow, Voxel51 (FiftyOne), Deci, Edge Impulse, NVIDIA DeepStream, Seldon, Triton (GPU).

### Metrics
mAP, IoU, Dice, FPS, latency, GPU utilization, label cost/item, annotation agreement.

---

## QAOps (`QAOps/`)
QA + DevOps. Testing embedded in pipeline; "quality is everyone's job".

### Scope
Unit → integration → contract → e2e → performance → security → accessibility → regression. All automated, gated in CI.

### Key practices
- **Shift-left testing** — early, often.
- **Test pyramid** — many unit, fewer integration, fewest e2e.
- **Contract testing** (Pact, Spring Cloud Contract).
- **Mutation testing** (Pitest, Stryker, mutmut).
- **Property-based testing** (Hypothesis, QuickCheck, fast-check).
- **Visual regression** (Percy, Chromatic).
- **Load / stress** (k6, Gatling, Locust, JMeter).
- **Chaos testing** (Chaos Monkey, Gremlin, Litmus).
- **Test data management** — synthetic data + masking.
- **Flaky test triage** — quarantine + fix.

### Metrics
Code coverage, mutation score, defect escape rate, test-suite flakiness, MTTR test failures, time-to-feedback in CI.

---

## FinOps (`FinOps/`)
Financial accountability for cloud + compute. Engineering ↔ Finance collaboration.

### Phases
1. **Inform** — visibility: tag, allocate, forecast.
2. **Optimize** — right-size, reserved/spot, autoscaling, idle cleanup.
3. **Operate** — embed in engineering culture; unit economics.

### Tools
AWS Cost Explorer, GCP Billing, CloudHealth, Kubecost, OpenCost, Vantage, Finout, Spot.io.

### Metrics
Cost per request / user / feature, utilization %, reserved coverage, waste %, cloud unit economics.

---

## SecOps (`SecOps/`)
Security operations — the SOC side. Monitoring, detection, incident response.

### Scope
SIEM, SOAR, EDR, XDR, threat intel, vulnerability management, incident response (NIST: Detect → Respond → Recover).

### Tools
Splunk, Elastic Security, Wazuh, CrowdStrike Falcon, SentinelOne, Microsoft Defender XDR, Sentinel, Chronicle, Tines, Torq.

### Metrics
MTTD, MTTR, dwell time, % alerts auto-triaged, backlog, false-positive rate.

---

## PlatformOps (`PlatformOps/`) / Platform Engineering
Build internal developer platform (IDP). Self-service, paved paths, golden templates.

### Scope
Developer portal (Backstage), service catalogs, scaffolding templates, built-in security + observability, T-shirt sized compute.

### Tools
Backstage (Spotify), Port, Cortex, Humanitec, CNOE, Crossplane.

### Metrics
Time-to-first-deploy for new service, developer NPS, % services on paved path, on-call load per team.

---

## Cross-discipline map

| Discipline | Core asset | Biggest failure mode | Distinct skill |
|------------|-----------|----------------------|----------------|
| DevOps | Code | Broken deploys | Pipelines + infra |
| DevSecOps | Code + policy | Vuln leaks to prod | Threat modeling |
| GitOps | Declarative state | Drift | Reconciliation |
| DataOps | Data pipelines | Stale / bad data | Lineage + quality |
| MLOps | Models | Drift in prod | Retraining infra |
| ModelOps | All models (risk) | Ungoverned models | Risk management |
| LLMOps | Prompts + models | Hallucination, cost | Prompt eng + eval |
| AIOps | Telemetry | Alert noise | Anomaly detect |
| CVOps | Labeled images/video | Label drift, FPS miss | Labeling + edge |
| QAOps | Tests | Flaky / missing tests | Test strategy |
| FinOps | Cloud bill | Waste | Tagging + forecasting |
| SecOps | Telemetry + signals | Breach | IR + threat intel |
| PlatformOps | Dev platform | Snowflake services | Abstraction design |

## Lifecycle template (any Ops)
```
Plan → Define metrics (SLIs/SLOs)
     → Automate pipeline (CI/CD/CT for your asset)
     → Observability (logs/metrics/traces + domain-specific signals)
     → Incident response (alert → runbook → remediation → postmortem)
     → Continuous improvement (retro, metric review, policy update)
```

## Reading list
- *The DevOps Handbook* — Kim, Humble, Debois, Willis.
- *Accelerate* — Forsgren, Humble, Kim (DORA).
- *Designing Machine Learning Systems* — Chip Huyen.
- *Machine Learning Engineering* — Andriy Burkov.
- *Implementing MLOps in the Enterprise* — Haviv & Gift.
- *Building LLM Powered Applications* — Valentina Alto.
- *Platform Engineering* — Camille Fournier et al.
- *Cloud FinOps* — Storment & Fuller.
