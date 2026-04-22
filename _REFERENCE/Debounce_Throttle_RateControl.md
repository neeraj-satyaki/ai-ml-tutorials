# Debounce, Throttle, Rate Control

Family of techniques that tame event bursts or limit call rates. All related, all different. Pick by intent.

---

## 1. Semantics at a glance

| Technique | Core idea | Fires when |
|-----------|-----------|------------|
| **Debounce** | wait for quiet period | only after N ms of no new calls |
| **Throttle** | cap call rate | at most once per N ms |
| **Rate limit** | global budget | drop/queue when budget exhausted |
| **Coalesce** | merge in-flight duplicates | one call handles many callers |
| **Backpressure** | slow producer | consumer signals "too fast" |
| **Sampling** | keep a fraction | 1 in N or random p |
| **Batching** | buffer + flush | at size or time |

---

## 2. Debounce

**Use when:** burst of events, you only care about the *last* one (or first).

### Trailing debounce (default)
Fire handler `N ms` after the last call. Typical: search-as-you-type, autosave, window resize.

```js
function debounce(fn, wait) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), wait);
  };
}
// usage
input.addEventListener("input", debounce(e => search(e.target.value), 300));
```

### Leading debounce
Fire once on the first call, ignore the rest until quiet.

### Leading + trailing
Fire on first call AND after the last; lodash `_.debounce(fn, wait, { leading: true, trailing: true, maxWait })`.

### `maxWait`
Prevents starvation: if calls never stop, force-fire every `maxWait ms`.

---

## 3. Throttle

**Use when:** continuous stream of events, run handler at fixed max rate.

Typical: scroll, mousemove, gamepad poll, sensor stream, metric emission.

```js
function throttle(fn, wait) {
  let last = 0, t;
  return (...args) => {
    const now = Date.now();
    const rem = wait - (now - last);
    if (rem <= 0) { last = now; fn(...args); }
    else {
      clearTimeout(t);
      t = setTimeout(() => { last = Date.now(); fn(...args); }, rem);
    }
  };
}
```

Variants: leading-only (drop trailing), trailing-only, both (lodash default).

### Throttle vs Debounce — one-liner
- **Throttle** = fire often, spaced out.
- **Debounce** = fire once, after quiet.

Search input: **debounce**.
Scroll handler: **throttle**.

---

## 4. `requestAnimationFrame` throttle (browser)

Pair per-frame events (scroll, mousemove) to display refresh:
```js
let ticking = false;
window.addEventListener("scroll", () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => { update(); ticking = false; });
});
```
Gives 60 Hz cap (or 120 on ProMotion) without timers.

---

## 5. `requestIdleCallback`

Run on idle CPU. Good for non-critical analytics, cache warming.

---

## 6. Rate limiting (backend)

**Use when:** protect services from clients. Fairness across tenants.

### Token bucket
Bucket holds tokens; each request consumes one. Refills at fixed rate `r`, cap at `B`. Allows bursts up to `B`.

### Leaky bucket
Queue + fixed-rate drain. Smooths bursts but doesn't allow them.

### Fixed window
Count calls in current second/minute. Simple; suffers at window edges.

### Sliding window (counter / log)
Smoothed fixed-window; closer to real rate.

### GCRA (Generic Cell Rate Algorithm)
Continuous equivalent of leaky bucket. Used by Cloudflare, Stripe. O(1) state per key.

### Python token-bucket example
```python
import time
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate, self.cap = rate, capacity
        self.tokens = capacity
        self.t = time.monotonic()
    def take(self, n=1):
        now = time.monotonic()
        self.tokens = min(self.cap, self.tokens + (now - self.t) * self.rate)
        self.t = now
        if self.tokens >= n:
            self.tokens -= n
            return True
        return False
```

### Where to enforce
- **Edge** (CDN / WAF / API Gateway) — cheapest, protects origin.
- **Service** — per-tenant, business-logic aware.
- **DB / downstream** — circuit breakers + bulkheads.

### Distributed rate limiting
Redis + Lua script (atomic). `redis-cell` module implements GCRA natively. Cloud primitives: AWS API Gateway usage plans, Cloudflare Rate Limiting.

---

## 7. Coalescing (request dedup)

Multiple concurrent callers requesting same key → merge into one downstream call, share result.

```python
import asyncio
inflight = {}
async def coalesced(key, fetch):
    if key in inflight: return await inflight[key]
    fut = asyncio.ensure_future(fetch())
    inflight[key] = fut
    try: return await fut
    finally: inflight.pop(key, None)
```

Same idea: **singleflight** (Go `golang.org/x/sync/singleflight`), React `useSWR`, `@tanstack/query` dedup.

Kills cache stampede + thundering herd on cold caches.

---

## 8. Backpressure

Consumer tells producer "slow down" instead of buffering unbounded.

Signals:
- TCP flow control (receive window).
- HTTP/2 stream flow control.
- gRPC + reactive streams (Project Reactor, RxJS `throttle`/`sample`/`window`).
- Node streams (`readable.pause()` / `resume()`).
- Kafka consumer lag → pause + reduce publish rate.
- Bounded queues with blocking put (Java `BlockingQueue`, Go buffered channel full).

---

## 9. Retry + backoff + jitter

Related family — don't hammer a failing service.

- **Exponential backoff**: delay = base × 2^attempt.
- **Full jitter** (AWS recommended): `delay = random(0, base × 2^attempt)`.
- Cap max delay.
- Cap max retries.
- Combine with **circuit breaker** to short-circuit known-bad dependencies.

```python
import random, time
def retry(fn, tries=5, base=0.1, cap=30):
    for i in range(tries):
        try: return fn()
        except Exception:
            if i == tries - 1: raise
            time.sleep(min(cap, random.uniform(0, base * 2**i)))
```

---

## 10. Circuit breaker

After `N` failures in `W` window, open circuit → fail fast. Half-open after cooldown to test.

Libraries: Resilience4j (Java), Polly (.NET), `opossum` (Node), Hystrix (legacy).

---

## 11. Sampling

When emitting lots of signals (logs, metrics, traces), sample:
- Uniform (every Nth).
- Probabilistic (p per event).
- Head-based (trace sampled by root service).
- Tail-based (decide after trace done — keep slow/error ones).

Trade: signal fidelity vs cost.

---

## 12. Batching

Buffer events; flush at size or time.
- Tracing: OTel batch span processor (5s or 512 spans).
- Logs: file handler buffer.
- DB: multi-insert.
- GPU: continuous batching (vLLM).

---

## 13. Choosing the right one

| Scenario | Use |
|----------|-----|
| Search input box | Debounce (trailing, 200-300 ms) |
| Scroll position update | Throttle or `requestAnimationFrame` |
| Window resize | Debounce (150-300 ms) |
| Save on typing pause | Debounce + `maxWait` |
| Slider value → heavy recalc | Throttle (50-100 ms) |
| API per-user protection | Token bucket rate limit |
| Public API global protection | Fixed window at gateway + GCRA per key |
| Cache miss storm | Coalesce (singleflight) |
| Kafka consumer fast producer | Backpressure via consumer pause |
| Flaky downstream | Retry + jitter + circuit breaker |
| Logs volume explosion | Sampling + batching |
| Expensive metric collection | Sampling |

---

## 14. Common bugs

- Debounce without `clearTimeout` in React → new timer per render. Use `useMemo`/`useRef` to keep stable.
- Throttle ignored by timestamp drift — use monotonic clock on backends.
- Rate limiter not atomic in multi-node setup — use Redis-Lua or GCRA.
- Exponential backoff **without jitter** → thundering herd retries.
- Debounce loses last event when component unmounts → flush on cleanup.
- `setTimeout` delay varies under load — don't assume exact timing.

## 15. Libraries

**Frontend/JS**
- `lodash.debounce`, `lodash.throttle`.
- **RxJS**: `debounceTime`, `throttleTime`, `auditTime`, `sampleTime`, `bufferTime`.
- React: `useDeferredValue`, `useTransition`, custom hooks (`use-debounce`).

**Backend**
- Go: `golang.org/x/time/rate`, `singleflight`.
- Python: `aiolimiter`, `ratelimit`, `tenacity` (retry).
- Java: Resilience4j, Guava `RateLimiter`.
- Redis: `redis-cell`, Lua scripts.
- Node: `bottleneck`, `p-limit`, `async-retry`.

## 16. Relation to this repo
Fits under `Frontend/Performance`, `Backend/APIs` rate-limit section, `SystemDesign/Patterns/RateLimiting`, `DesignPatterns/Cloud_Native/Throttling`, `Ops/SecOps` (DDoS), `DL/ComputerVision/Streaming` (backpressure on frame pipelines).
