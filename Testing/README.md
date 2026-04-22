# Testing — All Types

Cross-cutting discipline. Test pyramid: many unit → some integration → few E2E. Plus mutation, property-based, fuzz, visual, a11y, chaos, perf, security, ML.

## Unit (`Unit/`)
xUnit style: JUnit, NUnit, pytest, Jest, Vitest, Go testing, `cargo test`, RSpec. Mocks / stubs / spies. Fixtures + test data builders. Parameterized tests. Snapshot tests.

## Integration (`Integration/`)
- **Testcontainers** (Java/Python/Node/Go) — spin real DB/Kafka/Redis.
- Docker Compose for tests.
- Hermetic environments.
- **Contract testing**: Pact, consumer-driven contracts.
- Migrations exercised in test setup.
- API contract tests vs OpenAPI.

## End-to-End (`EndToEnd/`)
- **Playwright** (modern default), **Cypress**, Selenium WebDriver.
- Mobile: **Detox** (RN), XCUITest (iOS), Espresso (Android), **Appium**.
- Device clouds: BrowserStack, SauceLabs.

## Property-based (`PropertyBased/`)
Specify invariants; framework generates test cases.
- **Hypothesis** (Python), **fast-check** (JS), **QuickCheck** (Haskell / Erlang), PropCheck (Elixir), ScalaCheck, Jqwik (Java).

## Fuzz (`Fuzz/`)
Random / coverage-guided input generation.
- **libFuzzer**, **AFL++**, **honggfuzz**.
- `cargo-fuzz`, Go native fuzz, Jazzer (Java), Atheris (Python).
- Structure-aware fuzzing (protobuf, grammar-based).
- Differential fuzzing (compare two implementations).

## Mutation (`Mutation/`)
Are tests actually catching bugs? Mutate source, rerun tests.
- **PIT / Pitest** (Java), **Stryker** (JS/C#), **mutmut** (Python), Mull (LLVM/C/C++), Mutant (Ruby).

## Performance (`Performance/`)
- **k6**, **Gatling**, **Locust**, **wrk**, **vegeta**, **JMeter**.
- Benchmark harnesses: Criterion (Rust), Google Benchmark (C++), pytest-benchmark, JMH (Java).
- Flame graphs: Pyroscope, Parca, py-spy, `perf`.

## Security (`Security/`)
- **ZAP** baseline / full scans.
- **Nuclei** templates.
- **Semgrep**, **CodeQL** custom rules.
- DAST in CI. IAST runtime instrumentation.
- Supply chain: Sigstore / cosign verify in pipeline.

## Chaos / Resilience (`Chaos_Resilience/`)
- **Chaos Mesh**, **Gremlin**, **Litmus**, **Pumba** (Docker).
- Failure injection (HTTP 5xx, latency).
- NetEm (latency/loss), disk pressure.
- Game days, red-team drills.

## Visual regression (`VisualRegression/`)
- **Percy**, **Chromatic** (Storybook), BackstopJS, Applitools, `reg-suit`, pixelmatch.

## Accessibility (`Accessibility/`)
- **axe-core**, Pa11y, Lighthouse CI (a11y audits).
- Screen-reader automation (VoiceOver, NVDA).
- Keyboard-only test flows.

## ML Testing (`MLTesting/`)
- Data schema tests: **Great Expectations**, Soda, Pandera.
- Model behavior tests: **CheckList** (Ribeiro), invariance + directional expectation tests.
- Drift alerts in CI.
- Shadow / A-B model tests.
- Golden-set evals.
- LLM-as-judge evals with rubrics.

## Rules
1. Pyramid: test cost × count inversely related.
2. Fast unit tests (< 100 ms each); slow suites kill engineering velocity.
3. No flaky tests — quarantine + fix with deadline.
4. Coverage % is vanity, mutation score is sanity.
5. Every reported bug → first write a regression test, then fix.

## Books + refs
- *Growing Object-Oriented Software, Guided by Tests* — Freeman & Pryce.
- *xUnit Test Patterns* — Meszaros.
- *The Art of Unit Testing* — Osherove.
- *Property-Based Testing with PropEr, Erlang, and Elixir* — Hébert.
- *Beyond Behavior-Driven Development* — etc.
