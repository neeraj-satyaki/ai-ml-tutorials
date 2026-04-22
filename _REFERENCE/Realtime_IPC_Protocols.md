# Real-Time, Messaging & IPC Protocols — Full Comparison

Every way two processes/services/clients talk. Pick by: direction (push/pull/duplex), guarantees (ordering, delivery, durability), scale, latency, infra, browser-reachable?

---

## 1. One-shot / request-response

| Protocol | Notes |
|----------|-------|
| **HTTP/1.1** | Ubiquitous. Keep-alive, no multiplex. Head-of-line blocking. |
| **HTTP/2** | Binary, multiplexed streams over one TCP. Server push (deprecated). |
| **HTTP/3 (QUIC)** | UDP-based. No HOL blocking at transport. Faster handshake (0-RTT). |
| **gRPC** | HTTP/2 + protobuf. Typed contracts. Unary + streaming modes. |
| **JSON-RPC, XML-RPC** | Simple RPC over HTTP. |
| **GraphQL** | HTTP POST with flexible query. Subscriptions = WebSocket/SSE. |
| **tRPC** | TypeScript RPC; infers types across client/server. |
| **SOAP** | Legacy; still in enterprise/govt. |

## 2. Server → client push

| Protocol | Direction | Best for |
|----------|-----------|----------|
| **Webhooks** | server → server HTTP POST | async event delivery (Stripe, GitHub, Slack) |
| **Long polling** | client pulls, server holds | simple pre-WebSocket fallback |
| **Server-Sent Events (SSE)** | server → browser, uni-dir | stream of LLM tokens, live feeds, notifications |
| **HTTP/2 push** | deprecated | gone in Chrome 106+ |
| **WebSockets** | full-duplex | chat, collab, gaming, live dashboards |
| **WebTransport** | QUIC-based, HTTP/3 | modern replacement for WebSocket + datagrams |
| **WebRTC DataChannel** | P2P over ICE/STUN/TURN | low-latency browser-to-browser |
| **gRPC server-streaming** | server → client | typed streams backend services |

## 3. Full duplex / bi-directional

- **WebSockets** — browser + server, TCP, ordered, single connection.
- **gRPC bidirectional streaming** — backend, HTTP/2.
- **WebTransport** — HTTP/3; reliable streams + unreliable datagrams in same session.
- **WebRTC** — P2P media + data; STUN/TURN/ICE for NAT traversal.
- **Raw TCP/UDP** — custom protocols, non-browser.

## 4. Messaging / event brokers

| Broker | Model | Durability | Typical latency |
|--------|-------|------------|-----------------|
| **Kafka** | append-only log, partitioned | disk, replicated | ms |
| **RabbitMQ** | queue + routing (AMQP) | disk | sub-ms |
| **NATS** | subject-based pub/sub + JetStream | mem + disk | µs-ms |
| **Redis Streams / Pub/Sub** | in-mem log | memory (+AOF) | µs |
| **Redpanda** | Kafka-compatible, Raft native | disk | ms |
| **Apache Pulsar** | tiered storage, multi-tenant | disk | ms |
| **AWS SQS** | managed queue | managed | 10s of ms |
| **AWS SNS** | pub/sub fan-out | managed | 10s of ms |
| **Google Pub/Sub**, **Azure Service Bus** | managed | managed | ms |
| **ZeroMQ / nanomsg** | brokerless socket lib | none | µs |
| **ROS 2 DDS** | pub/sub for robotics | config | µs-ms |
| **MQTT** | lightweight pub/sub, IoT | broker-config | ms |
| **AMQP 0.9.1 / 1.0** | formal messaging spec | broker-config | ms |
| **STOMP** | text-based, simple | broker-config | ms |

## 5. IoT / constrained

- **MQTT** (with QoS 0/1/2) — TCP; dominant IoT broker protocol.
- **MQTT-SN** — sensor networks, UDP.
- **CoAP** — UDP-based REST for constrained devices.
- **LoRaWAN** — long-range, low-power WAN.
- **Zigbee, Z-Wave, Thread, Matter** — mesh.
- **BLE GATT** — short-range.

## 6. Broadcast media / telco

- **RTP / RTCP** — real-time media over UDP.
- **RTSP** — session control for IP cameras.
- **RTMP** — legacy ingest to streaming platforms.
- **HLS / DASH** — adaptive playback over HTTP.
- **LL-HLS / LL-DASH** — low-latency variants.
- **SRT** — secure reliable transport, broadcast contribution.
- **WebRTC** — low-latency video, browser-native.
- **SMPTE ST 2110 + Rivermax** — uncompressed broadcast IP. See `_REFERENCE/Rivermax.md`.
- **eCPRI, CPRI** — 5G fronthaul.

## 7. Intra-host IPC

| Mechanism | Scope | Notes |
|-----------|-------|-------|
| **Shared memory** (`shm_open`, mmap, tmpfs) | same host | fastest; locks needed |
| **Unix domain sockets** | same host | stream or datagram |
| **Named pipes (FIFOs)** | same host | byte stream |
| **POSIX message queues** | same host | priority + fixed size |
| **signalfd, eventfd** | same host | lightweight notification |
| **D-Bus** | same host | desktop services |
| **gRPC over Unix socket** | same host | structured RPC locally |
| **io_uring** | same process → kernel | async I/O primitives |
| **XDP / eBPF maps** | kernel ↔ user | very fast network paths |

## 8. High-performance / low-latency

- **Kernel bypass**: DPDK, XDP, Onload (Solarflare), VPP.
- **RDMA**: InfiniBand verbs, RoCEv2, iWARP. Zero-copy user ↔ user.
- **NVIDIA GPUDirect RDMA**: NIC → GPU memory direct.
- **Rivermax**: SMPTE 2110 + RoCE pacing (see separate doc).
- **ZeroMQ, Aeron** — low-latency messaging libs.
- **Chronicle Queue** — off-heap persisted, nanosec reads.
- **shared memory + atomics** — SPSC ring buffers for HFT.

## 9. Choose-one cheatsheet

| Goal | Pick |
|------|------|
| Browser push (notifications, LLM tokens) | **SSE** |
| Browser chat / collab / trading UI | **WebSockets** (or WebTransport) |
| P2P video call | **WebRTC** |
| Sending async events between companies | **Webhooks** |
| Typed RPC between microservices | **gRPC** |
| Low-latency file-ish streams same host | **Unix domain sockets** |
| Event log / replay / analytics | **Kafka / Redpanda** |
| Request-response with fan-out | **RabbitMQ** or **NATS** |
| Fan-out to SMS/email/push | **SNS → SQS** |
| IoT telemetry | **MQTT** |
| Constrained UDP device | **CoAP** |
| Broadcast 4K uncompressed video | **Rivermax** + SMPTE 2110 |
| Adaptive video playback | **HLS/DASH**, or **LL-HLS** |
| HFT order stream | Kernel-bypass UDP multicast / RDMA |
| Browser ↔ Node in same tab | **WebSockets** or BroadcastChannel |
| Same-machine Python ↔ Rust | shared memory / UDS / gRPC-UDS |
| Robot pub/sub | **ROS 2 DDS** |
| Multi-datacenter guaranteed delivery | **Kafka MirrorMaker / Pulsar Geo-Replication** |

## 10. Guarantees quick reference

| Property | What |
|----------|------|
| **At-most-once** | never duplicate; may lose |
| **At-least-once** | never lose; may duplicate (idempotency required) |
| **Exactly-once** | hard; Kafka idempotent producer + transactions, or app-level idempotency keys |
| **Ordering** | per-partition (Kafka), per-session (WS), none by default (UDP) |
| **Durability** | acks to quorum + disk fsync |
| **Ordered + durable + exactly-once** | the "transactional outbox" pattern in your app |

## 11. Webhook specifics

- POST body with HMAC-SHA256 signature header (Stripe: `Stripe-Signature`).
- Must verify signature + timestamp window to prevent replay.
- Idempotency key per event.
- Retries with exponential backoff on 5xx.
- Subscribers should respond quickly (< 5 s) and process async.
- Tools: webhook.site, ngrok, smee.io for local dev.

## 12. WebSocket specifics

- Handshake upgrades from HTTP.
- Sub-protocols negotiated via `Sec-WebSocket-Protocol`.
- No built-in reconnect — use libs (Socket.IO, reconnecting-websocket) or SSE as fallback.
- Scale via sticky sessions or pub/sub bus (Redis, NATS) to broadcast across servers.
- Auth: pass JWT in subprotocol or first message; cookies work but CSRF risk.
- Frame size limit; heartbeats (ping/pong) to detect dead conns.

## 13. SSE specifics

- HTTP GET with `Content-Type: text/event-stream`.
- Browser auto-reconnects, can resume with `Last-Event-ID`.
- One-way server → client. Browser sends via separate HTTP.
- No binary support (text only).
- Great for streaming LLM tokens, dashboards, notifications.

## 14. Anti-patterns

- Using WebSockets when SSE is enough — more infra for no benefit.
- Webhooks without signature verification.
- Kafka for tiny traffic (10 msg/s) — RabbitMQ/NATS simpler.
- Polling every 500 ms in a UI — use SSE / WS / WebTransport.
- Reinventing queue semantics on top of an RDBMS (mostly fine but verify performance).
- Fire-and-forget webhook without retries → lost events.

## 15. Relation to this repo

- Referenced by `Backend/APIs/`, `Frontend/`, `DL/ComputerVision/Streaming.md`, `_REFERENCE/Rivermax.md`, `_REFERENCE/Streaming_Frameworks.md`, `NetworkSecurity/README.md`, `SystemDesign/Networking/`.
- For rate-control of these channels see `_REFERENCE/Debounce_Throttle_RateControl.md`.
- Messaging-broker deep dive lives in `SystemDesign/Messaging/` and `Backend/MessagingJobs/`.
