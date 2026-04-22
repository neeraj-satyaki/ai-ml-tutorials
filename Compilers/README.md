# Compilers

Frontend → IR → Optimization → Backend → Runtime. Beyond `CS/Systems/Compilers`.

## Frontend
- **Lex** → tokens (Flex, ANTLR, hand-written). PEG parsers. Parser combinators. LL / LR / LALR generators. AST design. Semantic analysis. Type checking (Hindley-Milner). Name resolution + scoping. Macro expansion. Desugaring passes.

## IR (Intermediate Representation)
- **SSA form**, CFG + basic blocks, 3-address code.
- **LLVM IR**, **MLIR** (multi-dialect), GCC GIMPLE/RTL, **SPIR-V** (GPU), QBE, **Wasm IR**.
- Rust HIR → MIR → LLVM.
- JVM bytecode, CLR, CPython bytecode, Lua bytecode.
- CPS + ANF for functional languages.

## Optimization
- Classical: DCE, constant folding/prop, CSE, LICM, strength reduction, inlining, devirtualization, escape analysis, tail-call opt.
- **Vectorization** (SIMD auto-vec). Auto-parallelization. Loop transforms (unroll, tile, interchange). **Polyhedral** (Pluto).
- **PGO** (profile-guided). **LTO** (link-time). **Superoptimization** (Souper). Peepholes. Alias analysis.

## Backend
Instruction selection. **Register allocation** (linear scan, graph coloring). Scheduling (list prioritization). Calling conventions / ABI. Code layout (hot/cold). DWARF debug info. Exception handling / unwind. Relocations + PIC.

## Runtime
GC (mark-sweep, copying, generational, regional: ZGC/Shenandoah). Object headers + cards. Thread model. Stack maps + safepoints. Coroutine implementation. JIT tiers (interpreter → baseline → OSR → optimizing). Inline caches. Hidden classes / shape maps (V8). Tracing JITs (LuaJIT, PyPy). Wasm runtimes (Wasmtime, Wasmer, WAMR).

## Languages good for writing compilers
**Haskell**, **OCaml** (MenhirParsing), **Rust** (traits + proc macros), **Scala** (Meta-ALS), **Coq/Lean** (formally verified compilers), **C++** (LLVM ecosystem).

## Projects to build (hands-on ladder)
1. **TinyC-style** lexer + parser in Python / Rust.
2. ML-style interpreter with HM inference.
3. **LLVM frontend + pass**.
4. **MLIR dialect** + lowering.
5. JIT for a regex/query DSL.
6. **Wasm runtime**.
7. Stack language (Forth).
8. Lisp from scratch with macros.
9. Toy **borrow checker**.

## References
- **Dragon Book** — Aho, Sethi, Ullman, Lam.
- *Engineering a Compiler* — Cooper & Torczon.
- *Modern Compiler Implementation in ML* — **Appel** (Tiger Book).
- *Crafting Interpreters* — Nystrom (free online, best modern intro).
- *SSA-based Compiler Design* — Rastello & Tichadou (free).
- LLVM tutorial (kaleidoscope), MLIR tutorial.
- *Types and Programming Languages* — Pierce (for type systems).
