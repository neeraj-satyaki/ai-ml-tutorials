# Backend

Server-side engineering — runtimes, APIs, data, messaging, deploy.

## Languages / Runtimes (`Languages_Runtimes/`)
Node.js (V8, libuv), Deno, Bun. Python (CPython + asyncio). Go (goroutines, GMP). Rust + Tokio. JVM (Java/Kotlin). .NET (C#). Elixir (BEAM/OTP). Ruby, PHP, Scala (Akka), C++ servers, Swift-server.

## Web Frameworks (`Frameworks_Web/`)
Express/Koa/Fastify/NestJS. Next.js API routes. Django + DRF. FastAPI, Flask. Spring Boot + WebFlux. Rails. Laravel. ASP.NET Core minimal. Gin/Echo/Fiber (Go). Axum/Actix/Rocket (Rust). Phoenix/LiveView.

## APIs (`APIs/`)
REST + HATEOAS. GraphQL (Apollo, Relay, federation). gRPC + protobuf + streaming. JSON-RPC, tRPC. OpenAPI/Swagger/Postman. AsyncAPI. Webhooks. WebSockets. SSE. API Gateway patterns. Versioning. Rate limiting. Pagination (keyset/cursor). ETag / If-Modified-Since. Content negotiation.

## Data Layer (`DataLayer/`)
SQL vs NoSQL tradeoffs. ORMs (SQLAlchemy, Prisma, TypeORM, Hibernate, EF). Query builders (Knex, Kysely, jOOQ). Online migrations. Repositories + Unit of Work. CQRS (read/write models). Event sourcing. Transactional Outbox. Sharding impl. Database-per-service.

## Caching (`Caching/`)
Redis, Memcached. Local LRU (Caffeine). Look-aside, read-through, write-through, write-back. HTTP + CDN caching. Stale-while-revalidate. Cache stampede (coalescing, jitter, early refresh). Hot-key fan-out.

## Messaging / Jobs (`MessagingJobs/`)
Queues: Kafka, RabbitMQ, SQS, NATS, Pulsar, Redis Streams. Delayed + scheduled + cron. Idempotency + exactly-once semantics. DLQ. Retry + backoff. Job libs: Sidekiq, Celery, Bull, Hangfire, Resque. Workflow engines: Temporal, Cadence, Airflow, Prefect, Dagster.

## Auth (`Auth/`)
JWT design + pitfalls. Session vs JWT. OAuth2/OIDC flows (Auth Code + PKCE, Client Credentials, Device Code). SAML. Passport strategies. Multi-tenancy. Policy engines (Casbin, OPA). Row-level security. SSO (Clerk, Auth0, Cognito). Token refresh rotation + revocation.

## Observability / Reliability (`Observability_Reliability/`)
Structured logs. Prometheus/OpenMetrics. OpenTelemetry traces + exemplars. Health (live/ready/startup). Timeouts, retries + jitter, circuit breakers, bulkheads, backpressure, graceful shutdown, chaos testing.

## Security (`Security/`)
OWASP API Top 10. SQLi/XSS/CSRF/SSRF/XXE/IDOR. Rate limiting (token bucket, GCRA). Secrets management. Schema input validation (Zod, Pydantic, Joi). Audit logs. Encryption at rest + field-level. Tokenization. Privacy by default.

## Serverless + Edge (`Serverless_Edge/`)
AWS Lambda, Google Cloud Functions + Cloud Run, Azure Functions, Vercel Functions. Cloudflare Workers + Durable Objects. Deno Deploy. Fastly Compute@Edge. Bun Deploy. Cold-start strategies. Edge runtimes (V8 isolates, WASM).

## Microservices (`Microservices/`)
Service boundaries via DDD, DB-per-service, contracts. Service mesh (Istio, Linkerd). Saga orchestration vs choreography. Distributed tracing. Backwards-compatible rollouts. Canary + shadow traffic.

## Deployment (`DeploymentPacking/`)
Multi-stage Dockerfiles, OCI specs, buildpacks, distroless (Wolfi/Chainguard). K8s Deployments/StatefulSets/Jobs/CronJobs. Helm/Kustomize. ArgoCD Apps-of-Apps. Ingress/HTTPRoute.

## Performance (`Performance_Profiling/`)
Latency budgets. p50/p95/p99. Flame graphs (py-spy, perf, bpftrace). Heap profiling. IO-bound vs CPU-bound. Async best practices. Goroutine leak detection. Node event-loop blocking. Benchmarks (k6, vegeta, wrk).

## Books + Refs
- *Designing Data-Intensive Applications* — Kleppmann.
- *Release It!* — Nygard.
- *The Tangled Web* — Zalewski.
- *Fundamentals of Software Architecture* — Richards & Ford.
- *Software Engineering at Google* — Winters et al.
