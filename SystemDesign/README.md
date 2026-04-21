# System Design — Neck to Toe

Layered: Fundamentals → Building Blocks → Patterns → Scaling → Reliability → Security → Observability → DevOps → Case Studies → ML Systems.

---

## Fundamentals (`Fundamentals/`)
- **Scalability** — add capacity to handle growth (vertical / horizontal).
- **Latency** — time per request. p50 / p95 / p99 / p99.9.
- **Throughput** — requests/sec. Little's Law: L = λW.
- **Availability** — fraction of uptime. 99.9% = 8.76h/yr; 99.99% = 52min/yr.
- **Reliability** — correctness under failure.
- **Durability** — data survives failures.
- **Consistency Models** — strong, linearizable, sequential, causal, eventual, bounded staleness.
- **CAP** — under partition: choose C or A.
- **PACELC** — else (normal): latency vs consistency.
- **Fallacies of Distributed Computing** — network reliable/zero latency/etc. — all false.
- **Back-of-Envelope Estimation** — QPS × bytes × users; know L1=1ns, main mem=100ns, SSD=100µs, HDD=10ms, intra-DC RT=0.5ms, cross-region=100ms.
- **SLI / SLO / SLA** — indicator / objective / agreement.

---

## Networking (`Networking/`)
- **DNS** — hierarchical resolution; TTL trade-offs.
- **CDN** — edge caching (CloudFlare, Fastly, CloudFront); push vs pull.
- **Load Balancers** — L4 (TCP) vs L7 (HTTP). Algorithms: round robin, least-connections, weighted, consistent hash.
- **Reverse Proxy** — nginx, Envoy, HAProxy.
- **API Gateway** — Kong, Apigee, AWS API GW. AuthN, rate limit, routing.
- **TCP/UDP**, **HTTP/1.1, /2, /3 (QUIC)**, **WebSockets**, **SSE**, **webhooks**.
- **gRPC** — HTTP/2, protobuf, bidirectional streaming.
- **GraphQL** vs **REST** — flexible queries vs resource-oriented.
- **TLS / mTLS** — cert-based authn both ways.
- **Service Mesh** — Istio, Linkerd. mTLS + traffic control + observability sidecars.

---

## Storage (`Storage/`)
- **Block** — raw devices; EBS, iSCSI.
- **Object** — S3, GCS, Azure Blob; flat KV of blobs + metadata.
- **File** — POSIX semantics; NFS, EFS.
- **Relational DB** — Postgres, MySQL; strong typing, joins, ACID.
- **NoSQL** — KV (Redis, DynamoDB), Document (MongoDB), Column (Cassandra, HBase), Graph (Neo4j, JanusGraph).
- **NewSQL** — Spanner, CockroachDB, TiDB, YugabyteDB.
- **Time Series** — InfluxDB, Prometheus, Timescale, Druid, Clickhouse.
- **Vector DB** — Pinecone, Weaviate, Milvus, Qdrant, pgvector.
- **Search** — Elasticsearch, OpenSearch, Meilisearch, Typesense.
- **In-Memory** — Redis, Memcached, Dragonfly, KeyDB.
- **Columnar Warehouse** — BigQuery, Snowflake, Redshift, Clickhouse.
- **Data Lake** — S3 + Iceberg / Delta / Hudi (open table formats).
- **Lakehouse** — Databricks pattern: warehouse on lake.

---

## Databases Deep (`Databases/`)
- **Indexing** — B-tree (range), LSM-tree (write-heavy), Hash (point), Inverted, GIN/GIST.
- **Query Planning** — cost-based optimizer; stats; EXPLAIN.
- **Normalization / Denormalization** — 1NF-5NF vs OLAP flattening.
- **Sharding** — range, hash, directory, consistent hash.
- **Replication** — leader-follower (most RDBMS), multi-leader (MySQL Group Rep), leaderless (Dynamo, Cassandra).
- **Transactions** — ACID vs BASE.
- **Isolation Levels** — Read Uncommitted / Read Committed / Repeatable Read / Serializable / Snapshot. Anomalies: dirty read, non-repeatable, phantom, write skew.
- **MVCC** — multi-version concurrency.
- **2PC / 3PC** — distributed atomic commit.
- **Paxos / Raft** — replicated log consensus.
- **CDC (Change Data Capture)** — Debezium, Postgres logical replication.
- **WAL** — write-ahead log for crash recovery.
- **Compaction** (LSM), **Vacuum** (MVCC), **Failover**, **Connection Pooling** (PgBouncer), **Prepared Statements**.

---

## Caching (`Caching/`)
- **Patterns** — Look-aside (cache-aside), Write-through, Write-back, Write-around.
- **Eviction** — LRU, LFU, FIFO, TTL, ARC, 2Q.
- **Cache Invalidation** — TTL, event-based, versioned keys. "Two hard problems: cache invalidation, naming, off-by-one."
- **CDN caching, Browser cache, App-level cache, Memcached vs Redis**.
- **Cache Stampede / Thundering Herd** — mitigation: request coalescing, early refresh, jitter, probabilistic early expiration.
- **Hotkey Handling** — request coalescing, local LRU before remote, read replicas, sharding.

---

## Messaging (`Messaging/`)
- **Queue vs PubSub** — point-to-point vs broadcast.
- **Kafka** — partitioned log; consumer groups; offsets; exactly-once via idempotence + transactions.
- **RabbitMQ, SQS/SNS, NATS** — alternative brokers.
- **Event Sourcing** — store events, not state; replayable.
- **CQRS** — command / query segregated models.
- **Outbox Pattern** — transactional message publish.
- **Idempotency Keys** — safe retries.
- **Delivery** — at-most-once, at-least-once, exactly-once.
- **Dead Letter Queue** — failed messages.
- **Back-Pressure** — slow consumer, buffer; flow control.
- **Stream Processing** — Flink, Spark Streaming, Beam, Kafka Streams.
- **Windows** — tumbling, sliding, session; **Watermarks** handle late data.

---

## Patterns (`Patterns/`)
- **Monolith / Modular Monolith / Microservices / Serverless**.
- **Event-Driven**, **Saga** (long-running distributed txn: choreography vs orchestration).
- **Circuit Breaker** — open/half-open/closed; Hystrix style.
- **Bulkhead** — isolate resource pools.
- **Retry + exponential backoff + jitter**.
- **Timeout** — always. Defaults kill services.
- **Rate Limiting / Throttling** — token bucket, leaky bucket, fixed/sliding window.
- **Sidecar / Ambassador / Adapter** — Envoy/Istio pattern.
- **Strangler Fig** — gradual monolith→microservices.
- **Leader Election / Quorum / Gossip / Heartbeat / Health Check**.
- **Consistent Hashing / Rendezvous Hashing / Hash Ring** — minimize remap on node change.
- **GeoHashing** — spatial indexing for ride/delivery.

---

## Reliability + DR (`ReliabilityDR/`)
- **Redundancy** (N+1, N+2), **Multi-AZ**, **Multi-Region**, **Active-Active**, **Active-Passive**.
- **Failover**, **DR**, **RPO** (how much data loss OK), **RTO** (how fast back up).
- **Backups** — full, incremental, differential; Point-in-Time Restore.
- **Chaos Engineering** — Chaos Monkey, Gremlin; inject failures.
- **Degraded Mode** — serve stale/partial > outage.
- **Graceful Shutdown** — drain + SIGTERM.
- **Deploy strategies** — Blue-Green, Canary, Rolling, Shadow, Dark Launch.
- **Feature Flags** — LaunchDarkly, GrowthBook.
- **Kill Switch** — instant off-ramp.

---

## Security (`Security/`)
- **AuthN vs AuthZ**, **OAuth2 / OIDC**, **JWT**, **SAML**.
- **RBAC / ABAC / ReBAC**, **Zero Trust**.
- **E2E Encryption**, **TLS / PKI**, **Secrets Management** (Vault, KMS).
- **WAF**, **DDoS mitigation** (CloudFlare, Shield).
- **CSRF / XSS / SQLi** prevention.
- **Supply-Chain** — signed artifacts, SBOM (SPDX, CycloneDX), SLSA.
- **Compliance** — SOC2, GDPR, HIPAA, PCI-DSS.
- **Audit Logs**, **Encryption at rest + in transit**, **Key rotation**, **HSM**.

---

## Observability (`Observability/`)
Three pillars + more.
- **Logs** (structured JSON), **Metrics** (counter/gauge/histogram/summary), **Traces** (distributed, spans; OpenTelemetry).
- **APM** — Datadog, New Relic, Honeycomb.
- **RED method** (Rate, Errors, Duration) for services; **USE method** (Utilization, Saturation, Errors) for resources.
- **SLO burn-rate alerts**.
- **Alerting** — PagerDuty, Opsgenie.
- **Profiling** — CPU, heap, flame graphs; continuous (Pyroscope, Parca).
- **On-call playbooks**, **Blameless postmortems**.

---

## Scaling (`Scaling/`)
- Vertical vs Horizontal; Auto-scaling (HPA, VPA, Cluster Autoscaler).
- **Sharding strategies** — range, hash, directory; resharding painful.
- **Read-replica / Read-write split / DB federation**.
- **Multi-tenancy** — shared vs silo vs pool; per-tenant sharding.
- **Concurrency** — async (Node, asyncio), threads, actors (Erlang, Akka).

---

## DevOps + Infra (`DevOps_Infra/`)
- **IaC** — Terraform, Pulumi, CloudFormation.
- **Kubernetes** — pods, deployments, services, ingress; operators, CRDs; Helm, Kustomize.
- **GitOps** — Argo CD, Flux.
- **CI/CD** — GitHub Actions, GitLab CI, Jenkins, Buildkite.
- **Docker** — multi-stage builds, image optimization, registries.
- **FinOps** — spot, reserved, savings plans; right-sizing.
- **Multi/Hybrid cloud**, **Edge** (Cloudflare Workers, Fastly), **Serverless** (Lambda, Cloud Run).

---

## Case Studies (`CaseStudies/`)
How would you build…?
- **URL Shortener** — base62 + KV store + cache.
- **Pastebin / Dropbox** — blob storage + metadata DB + dedup (CAS).
- **Twitter feed** — fan-out on write vs read; hybrid.
- **Instagram** — media pipeline + feed + notifications.
- **YouTube / Netflix** — video encoding ladder, HLS/DASH, CDN, DRM.
- **Uber / Lyft** — geo-sharding + matching + surge.
- **DoorDash** — multi-sided marketplace + routing.
- **WhatsApp / Slack / Zoom** — real-time messaging, SFU vs MCU.
- **Google Search** — crawl → index → rank → serve.
- **Amazon/Netflix recommendations** — candidate gen → ranking.
- **Web Crawler** — polite BFS, dedup, robots.txt.
- **Rate Limiter** — token bucket distributed.
- **Distributed File System** — GFS/HDFS: NameNode + replicated chunks.
- **Distributed Cache**, **KV Store** (Dynamo, Cassandra).
- **Payments (Stripe)** — idempotent, ledger, reconciliation.
- **Notifications** — fanout + preferences + digest.
- **Ads Serving** — auction (GSP, VCG), sub-100ms budget.
- **E-commerce checkout** — inventory, saga, payments.
- **Google Maps driving directions** — contraction hierarchies.
- **Typeahead / AutoSuggest** — trie + popularity.
- **Collaborative Editor (Docs)** — OT or CRDT.
- **Stock Exchange** — FIX, order book, matching engine, microsecond latency.
- **Fraud Detection** — real-time features + scoring.
- **Booking (Airbnb)** — inventory + concurrent booking locks.
- **Metrics (Prometheus) / Logging (ELK)**.
- **Distributed Task Queue** (Celery, Sidekiq).
- **Distributed Lock** (Redis redlock, etcd, Zookeeper).
- **Pub/Sub** (Kafka, PubSub).
- **ChatGPT-like LLM serving** — token streaming, batching, GPU sharding.

---

## ML Systems (`MLSystems/`)
- **Feature Store** — Feast, Tecton. Offline + online, point-in-time correctness.
- **Model Registry** — MLflow, Weights & Biases artifacts.
- **Training Orchestration** — Kubeflow, Metaflow, Ray Train, SageMaker.
- **Distributed Training** — Data Parallel, DDP, FSDP (fully sharded), ZeRO 1/2/3, Tensor Parallel, Pipeline Parallel, 3D Parallel.
- **Serving** — online (low-latency) vs batch; Triton, TorchServe, TFServing, Ray Serve.
- **LLM Serving** — **KV Cache**, **Continuous Batching** (vLLM), **PagedAttention**, **Speculative Decoding**, **Quantization** (INT8, INT4, FP8, AWQ, GPTQ), **Pruning**, **Distillation**.
- **Retrieval / RAG Infra** — embedding service + vector DB + reranker.
- **GPU Scheduling** — NVIDIA MPS, MIG, K8s device plugins, GKE TPU/GPU pools.
- **MLOps CI/CD** — data + model versioning (DVC, LakeFS), pipelines.
- **Canary / Shadow deploys**, **A/B test models**, **Data/Concept drift monitoring**.
- **Cost** — GPU vs CPU; batch size vs latency budget.
- **Serving Engines** — Triton, TGI, vLLM, SGLang, LMDeploy, TensorRT-LLM.
- **Autoscaling GPU pods**, **Multi-model endpoints** (save $$).

---

## Interview Framework (use this)
1. **Clarify** — functional + non-functional (QPS, SLA, data size).
2. **Estimate** — back of envelope.
3. **API / data model**.
4. **High-level** — boxes & arrows.
5. **Deep dive** — 1-2 components.
6. **Scale / bottlenecks** — cache, shard, replicate.
7. **Reliability / security / observability**.

## Classics
- "Designing Data-Intensive Applications" — Kleppmann.
- "System Design Interview" vol 1+2 — Alex Xu.
- "Site Reliability Engineering" — Google.
- "Building Secure & Reliable Systems" — Google.
- "Database Internals" — Petrov.
