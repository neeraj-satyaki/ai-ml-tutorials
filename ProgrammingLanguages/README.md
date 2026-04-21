# Programming Languages + Advanced Coding Techniques

Most-used languages, paradigms, and advanced techniques real experts actually use.

## Top Languages (`TopLanguages/`)

### Systems / low-level
**C** — POSIX, kernels, embedded. Still lingua franca.
**C++** — games, HFT, systems, ML infra. Modern C++17/20/23.
**Rust** — memory-safe systems; async (Tokio). Kernel, CLI, infra, blockchain.
**Zig / Nim / Crystal / V / Odin** — new systems contenders.
**Assembly** (x86-64, ARM64, RISC-V) — last-mile perf + RE.

### Application / general
**Python** — ML, scripting, automation, web. CPython. PEP 695 types, asyncio.
**Go** — cloud infra, Kubernetes, services. Goroutines.
**Java** — enterprise, Android, JVM ecosystem. Records, sealed classes.
**Kotlin** — Android, server (Ktor), multiplatform.
**C# / .NET** — Windows, games (Unity), cross-plat servers.
**Swift** — iOS/macOS + server-side.
**JavaScript / TypeScript** — web, Node, Deno, Bun.

### Dynamic / scripting
**Ruby** (Rails), **PHP** (Laravel), **Lua** (embedded scripting, Neovim), **Dart** (Flutter), **Perl** (legacy + text-munging).

### Functional
**Haskell**, **OCaml**, **F#**, **Scala**, **Clojure** — FP production.
**Elixir/Erlang** — BEAM VM; fault-tolerant telecoms + WhatsApp-scale.
**Racket/Scheme/Lisp** — DSLs, research.

### Scientific / data
**R**, **MATLAB**, **Julia** (differentiable programming, HPC).
**Fortran** — still dominates supercomputing (weather, physics).

### New / emerging
**Mojo** (Modular; Python-superset for AI).
**Gleam** (BEAM + types).
**Roc** (pure FP, performance).
**Carbon** (Google, C++ successor experiment).

### Query / config / ops
**SQL** — non-negotiable.
**Bash / Shell**, **PowerShell** — ops.
**HCL** (Terraform), **YAML** (K8s), **Nix** (reproducible).

## Paradigms (`Paradigms/`)
Imperative, procedural, OO, functional, logic, declarative, event-driven, reactive, array-oriented (APL/J/K), concurrency-oriented (Erlang, Pony), dependently typed (Idris, Agda, Lean). Static vs dynamic, strong vs weak, nominal vs structural.

## Advanced Techniques (`AdvancedTechniques/`)

### Metaprogramming
- **C++ templates / `constexpr` / `consteval`** — compile-time computation.
- **Rust macros + proc macros** — hygienic macros + code gen.
- **Lisp macros** — code-as-data.
- **Python decorators**, **descriptors**, **metaclasses**.
- **TypeScript type-level** — conditional/template literal types as a mini programming language.

### Type-level magic
Phantom types, GADTs, higher-kinded types (Haskell/Scala), typeclasses/traits, effect systems (Eff, Effekt, Koka, Unison). Monads/Functors/Applicatives. Free monads + tagless final. Lenses/optics. Algebraic effects + handlers.

### Performance
Intrinsics (SIMD: SSE/AVX-512, NEON, SVE). Auto-vectorization. Branch prediction hints. Inline asm. Memory-mapped I/O.

### Lock-free + concurrent
CAS + ABA problem + hazard pointers + RCU + epoch-based reclamation. Wait-free algorithms. Thread-local storage. Fibers/green threads. Stackful vs stackless coroutines. Structured concurrency (Kotlin, Swift, Trio). Actor model (Erlang, Akka, Elixir). CSP channels (Go, Rust). Software Transactional Memory (Clojure, Haskell).

### Zero-cost abstractions
Rust: ownership, borrowing, lifetimes, move semantics. C++: RAII, perfect forwarding, CRTP, SFINAE/Concepts. Data-oriented design, ECS (games), AoS vs SoA.

### Memory
Arenas, bumps, slabs, pools. Custom allocators. GC tuning (G1, ZGC, Shenandoah). ARC (Swift/ObjC). Reference counting + weak refs. Profile-guided optimization (PGO) + LTO.

### Compilation
JIT tiers (interpreter → baseline → optimizing). Inline caches, PICs, escape analysis, partial evaluation. AOT vs JIT. Multi-stage programming. LLVM/MLIR/Cranelift backends. eBPF programs.

### WebAssembly
Core + advanced. Component Model + WASI. Isolates for multi-tenant safety.

### FFI
pyo3 (Py↔Rust), napi-rs (JS↔Rust), ctypes / CFFI (Py↔C), JNI (Java↔C), nif (BEAM↔native).

### Parsers + DSLs
Hand-written recursive descent. Parser combinators. PEG. LR/LALR generators. Attribute grammars. Internal vs external DSLs.

### Correctness
Property-based testing (Hypothesis/QuickCheck/fast-check). Fuzzing (cargo-fuzz, libFuzzer, Honggfuzz). Differential fuzzing. Mutation testing (PIT, mutmut). Symbolic execution (KLEE + Z3). Theorem provers (Coq, Isabelle, Lean 4). Formal methods (TLA+, Alloy, Dafny). Model checking (SPIN, CBMC). Design-by-contract (Eiffel, Ada).

### Data structures + algorithms (advanced)
Persistent data structures (Clojure, Immutable.js), HAMT trie maps, Bloom filter impl, sketches (Count-Min, HyperLogLog), LSH/MinHash, ANN (HNSW, FAISS). Bit-twiddling (popcnt/lzcnt/pdep/pext/BMI). SWAR. Cache-oblivious + cache-aware algorithms.

### GPU programming
CUDA, ROCm, SYCL, WebGPU. SIMT (warps + lane masks). Shared memory + bank conflicts. Tiling + kernel fusion. Tensor core programming. CUDA Graphs + streams. cuBLAS/cuDNN/Triton. Nsight profiling. Auto-tuning.

### Concurrency primitives (systems)
Futex, io_uring, epoll, kqueue, lock elision (HLE/TSX), HW transactional memory, NUMA-aware code, cache-line alignment (avoid false sharing), data-race freedom (happens-before). Memory models (C++, Java, Rust) — release/acquire, SC.

## Toolchain / Build (`ToolchainBuild/`)
GCC, Clang, MSVC, rustc. Linkers (ld/lld/mold). Build systems: Make, CMake, Meson, Bazel, Buck2, Gradle, Maven, sbt, Cargo, PNPM, npm, yarn, Nx, Turborepo. Package managers (pip/poetry/conda, npm/yarn/pnpm, cargo, go mod, maven, gradle, composer, bundler, hex, opam). Debuggers (GDB, LLDB, WinDbg, rr time-travel). Static analyzers (clang-tidy, PVS-Studio, CodeQL, SonarQube). Formatters (Prettier, Black, Rustfmt, Gofumpt). Linters (ESLint, Clippy, golangci-lint).

## Runtime Internals (`RuntimeInternals/`)
Interpreters vs compilers. Bytecode VMs (JVM, CLR, BEAM, LuaJIT). JIT tiering (interpreter → baseline → optimizing). GC types (STW, concurrent, incremental, generational, regional: ZGC/Shenandoah/G1/CMS). ARC. Reflection internals. Dynamic dispatch (vtable, type tags). Inline caches + PICs. Adaptive recompilation. Tiered compilation + OSR. Fiber internals.

## How to pick a language
| Goal | First pick | Alt |
|------|-----------|-----|
| Backend services | Go or TypeScript | Rust, Kotlin, Elixir |
| ML research | Python | Julia |
| Systems / OS / kernel | Rust or C++ | C, Zig |
| Embedded / MCU | C or Rust | C++ |
| iOS | Swift | Objective-C |
| Android | Kotlin | Java |
| Game engines | C++ | Rust, C# (Unity) |
| Data science | Python | R, Julia |
| HFT | C++ | Rust |
| Smart contracts | Solidity + Rust (Solana, Polkadot) | Move (Aptos/Sui) |
| CLI tools | Rust or Go | Zig |
| Web frontend | TypeScript | — |

## Depth-of-mastery tiers
- **Tier 1** (know it): 2 languages at expert; 1 FP; SQL + Bash.
- **Tier 2** (adventurer): +Rust/Go/Python breadth; read C/C++ fluently; Haskell or OCaml for FP depth.
- **Tier 3** (polyglot) — 5+ production-quality; research-paper reading comprehension in all paradigms.

## Books
- *Programming Language Pragmatics* — Scott.
- *Types and Programming Languages* — Pierce.
- *Structure and Interpretation of Computer Programs* — Abelson & Sussman.
- *Crafting Interpreters* — Nystrom.
- *Engineering a Compiler* — Cooper & Torczon.
- *The Rust Programming Language* (Klabnik & Nichols).
- *Effective Modern C++* — Meyers.
- *Concurrency in Go* — Cox-Buday.
- *Java Concurrency in Practice* — Goetz.
