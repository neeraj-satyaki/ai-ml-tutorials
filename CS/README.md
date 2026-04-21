# Computer Science — Basics to PhD

Coverage: data structures → algorithms → complexity theory → systems → PhD frontier.

---

## Basics (`Basics/`)
- **DataTypes** — primitive vs composite, endianness, ranges.
- **ControlFlow** — conditionals, loops, recursion → iteration.
- **MemoryModel** — stack vs heap, alignment, paging.
- **PointersReferences** — indirection, aliasing.
- **Recursion** — base + step; tail recursion.
- **OOP** — encapsulation, inheritance, polymorphism, SOLID.
- **FunctionalBasics** — pure functions, immutability, HOFs, closures, monads.

---

## Data Structures (`DataStructures/`)
| Structure | Key ops / use |
|-----------|---------------|
| Arrays | O(1) index, contiguous |
| LinkedLists | O(1) insert/delete given node |
| Stacks, Queues, Deques | LIFO, FIFO, both |
| HashMaps | O(1) avg lookup; collision strategies |
| Trees / BSTs | O(log n) ordered ops; AVL, Red-Black |
| Heaps | priority queue; O(log n) push/pop |
| Graphs | adj list/matrix |
| Tries | prefix queries |
| BloomFilters | prob set-membership |
| SegmentTrees / FenwickTrees | range queries |
| UnionFind | disjoint sets, O(α(n)) |
| SkipLists | prob balanced ordered set |
| B+Trees | disk-friendly; DB indexes |
| LSM-Trees | write-optimized; Cassandra, RocksDB |
| Persistent | immutable versioned (FP langs) |
| SuccinctStructures | near info-theoretic minimum space |

---

## Algorithms

### Sorting (`Sorting/`)
Bubble, Insertion, Selection (O(n²) teaching); Merge, Quick, Heap (O(n log n)); Counting, Radix, Bucket (linear when range bounded); Tim (Python/Java default); External (disk).

### Searching (`Searching/`)
Linear, Binary, Interpolation, Exponential, Ternary.

### Graph (`Graph/`)
- **BFS / DFS** — traversal.
- **Dijkstra** — shortest path, non-negative weights, O((V+E) log V).
- **BellmanFord** — handles negative edges; detects negative cycles.
- **FloydWarshall** — all-pairs, O(V³).
- **AStar** — Dijkstra + heuristic.
- **MST** — Kruskal (edge-sort + UF), Prim (priority queue).
- **TopologicalSort** — DAGs; dependency ordering.
- **SCC** — Tarjan, Kosaraju.
- **MaxFlow** — Ford-Fulkerson, Edmonds-Karp, Dinic's, Push-Relabel.
- **MinCut** — dual of max-flow.
- **Matching** — Hopcroft-Karp (bipartite), Hungarian (assignment).
- **Planarity** — Kuratowski, Boyer-Myrvold.

### Paradigms (`Paradigms/`)
- **DivideConquer** — split, solve, combine.
- **DynamicProgramming** — overlapping subproblems, optimal substructure.
- **Greedy** — local optimal → global (when matroid structure).
- **Backtracking / BranchAndBound** — systematic search + pruning.
- **Randomized** — Las Vegas (always correct) vs Monte Carlo (correct with prob).
- **Approximation** — α-approximation for NP-hard.
- **Online** — decisions without future knowledge; competitive ratio.
- **Streaming** — bounded memory, one pass; sketches (Count-Min, HyperLogLog).
- **Sublinear** — don't even read full input; property testing.

### String (`String/`)
KMP, Rabin-Karp, Boyer-Moore, Suffix Arrays/Trees/Automata, Z-function, Aho-Corasick (multi-pattern), Edit Distance (Levenshtein, Damerau).

### Geometry (`Geometry/`)
Convex hull (Graham scan, Andrew, Chan), closest pair (D&C), line sweep, Voronoi/Delaunay, KD-tree, range search.

### Numerical (`Numerical/`)
FFT (O(n log n) polynomial mul / convolution), Fast matmul (Strassen O(n^2.807), current best ω≈2.371), Gaussian Elimination, Numerical ODE (RK4), Linear Programming (Simplex, Interior Point).

---

## Complexity (`Complexity/`)

### Basics
Big-O / Θ / Ω / o / ω; amortized analysis (accounting, potential, aggregate); Master theorem for recurrences; decision vs optimization vs search.

### Classes
| Class | Meaning |
|-------|---------|
| **P** | poly-time deterministic |
| **NP** | poly-time verifiable (or nondet. accept) |
| **NP-Complete** | NP + every NP problem reduces to it (SAT, TSP-decision) |
| **NP-Hard** | every NP reduces to it, may not be in NP |
| **coNP** | complements of NP |
| **PSPACE** | poly-space |
| **EXPTIME / NEXPTIME** | exp-time |
| **L / NL** | log-space det/nondet |
| **BPP / RP / ZPP** | prob poly-time variants |
| **BQP** | bounded-error quantum poly-time |
| **PH** | polynomial hierarchy Σ_i / Π_i / Δ_i |
| **#P** | counting class; #SAT |
| **PP** | majority acceptance |

### Key Theorems
- **Cook-Levin** — SAT is NP-complete.
- **TimeHierarchy / SpaceHierarchy** — strict inclusion with more resources.
- **Savitch** — NSPACE(f) ⊆ DSPACE(f²); PSPACE = NPSPACE.
- **Immerman-Szelepcsényi** — NL = coNL.
- **Ladner** — if P≠NP, NP-intermediate problems exist.
- **Toda** — PH ⊆ P^#P.
- **PCP Theorem** — NP = PCP(log n, 1); basis of hardness of approximation.
- **Baker-Gill-Solovay** (Relativization barrier) — ∃ oracle A: P^A=NP^A and oracle B: P^B≠NP^B → P vs NP can't be settled by relativizing proofs.
- **Razborov-Rudich** (Natural Proofs) — barrier on certain lower-bound proofs.
- **Algebrization** (Aaronson-Wigderson) — another barrier.

### Hardness
- **Reductions** — Karp (many-one), Cook (Turing). Gap reductions for inapproximability.
- **Unique Games Conjecture** — implies tight inapproximability for many problems.
- **Average-case** — distributional hardness; basis of crypto.
- **Fine-grained** — SETH, 3SUM, APSP: conditional lower bounds on polynomial problems.
- **Parameterized** — FPT, W-hierarchy (W[1], W[2], ...); tractability in a parameter.

### Advanced
- **Circuit Complexity** — AC^i, NC^i, TC^i; constant-depth lower bounds; Monotone circuits.
- **Communication Complexity** — bits exchanged between parties; lower bounds via disjointness.
- **Query Complexity** — # oracle queries.
- **Proof Complexity** — lengths of refutations (Resolution, Frege, LK).
- **Descriptive Complexity** — complexity = logic expressibility (Fagin's theorem: NP = ESO).
- **Geometric Complexity Theory (GCT)** — Mulmuley's program toward P vs NP via representation theory / algebraic geometry.
- **Quantum Complexity** — QMA, QIP = PSPACE, BQP vs PH.
- **Interactive Proofs** — IP = PSPACE (Shamir); MIP = NEXPTIME; MIP* = RE (Ji et al. 2020).
- **Zero-Knowledge Proofs** — ZKP; foundation of modern crypto + blockchains.
- **Derandomization** — does BPP = P? Hardness vs randomness (Nisan-Wigderson, Impagliazzo-Wigderson).

---

## Computability (`Computability/`)
- **Turing Machines** — tape model; universal TM.
- **Variants** — nondet, multi-tape, 2-way; same computable class.
- **Church-Turing thesis** — all physically realizable computation = TM-computable.
- **Halting Problem** — undecidable (Turing 1936).
- **Rice's Theorem** — every nontrivial semantic property of programs is undecidable.
- **Recursion Theorem** — programs can reference their own code.
- **Decidability vs Enumerability** — r.e. vs recursive vs co-r.e.
- **Degrees of Unsolvability** — Turing degrees; Post's problem (Friedberg-Muchnik).
- **Kolmogorov Complexity** — K(x) = shortest program output x. Incomputable.
- **Gödel Incompleteness** — any consistent r.e. arithmetic theory is incomplete.

---

## Formal Languages (`FormalLanguages/`)
- **Regular** — DFA / NFA / regex; pumping lemma.
- **Context-Free** — PDA, CFG; pumping lemma for CFL.
- **Context-Sensitive** — LBA; decidable membership.
- **Chomsky Hierarchy** — regular ⊂ CFL ⊂ CSL ⊂ RE.
- **Parsing** — LL(k), LR(k), LALR, GLR, Earley, CYK.
- **Grammars & Derivations** — leftmost, rightmost, ambiguity.
- **Semantics** — Operational (SOS, abstract machines), Denotational (domain theory), Axiomatic (Hoare logic).

---

## Systems (`Systems/`)
- **Architecture / ISA** — RISC vs CISC; x86, ARM, RISC-V.
- **Memory Hierarchy** — registers → L1/L2/L3 → DRAM → disk.
- **Pipelining / Superscalar** — ILP; hazards; OoO execution.
- **OS** — processes, threads, scheduling (CFS, O(1)), virtual memory (paging, TLB), file systems (ext4, ZFS).
- **Networking** — TCP/IP, UDP, HTTP/2/3, QUIC, DNS.
- **Databases** — relational algebra, query planning, indexes, transactions (ACID), isolation, MVCC.
- **NoSQL** — KV, document, columnar, graph.
- **Compilers** — lex/parse/AST/IR/optimize/codegen; SSA, register allocation.
- **Type Systems** — Hindley-Milner, System F, dependent types (Coq, Agda, Lean).
- **Garbage Collection** — mark-sweep, copying, generational, ref counting, tri-color.

---

## Parallel + Distributed (`Parallel_Distributed/`)
- **Concurrency** — locks, mutexes, semaphores, monitors; deadlock (4 conditions).
- **Lock-Free** — CAS, ABA problem, hazard pointers, RCU.
- **Memory Models** — sequential consistency, TSO, release/acquire.
- **MapReduce**, **MPI**, **OpenMP**, **CUDA** (GPU parallelism).
- **PRAM Models** — theoretical parallel machine.
- **Consensus** — Paxos, Raft, ZAB.
- **CAP / PACELC** — C-A-P under partition; L-A latency tradeoff under normal.
- **Consistency Models** — linearizable, sequential, causal, eventual.
- **Byzantine** — PBFT, HotStuff; tolerate arbitrary faults.
- **Blockchain** — Nakamoto consensus (PoW), PoS, DAG protocols.
- **Eventual Consistency** — CRDTs, OT.
- **DHT / Gossip** — Chord, Kademlia, scuttlebutt.
- **Vector / Logical Clocks** — Lamport, vector, hybrid logical clocks.
- **Distributed Snapshots** — Chandy-Lamport.
- **Leader Election** — Bully, Raft leader.

---

## Crypto + Security (`Crypto_Security/`)
Symmetric (AES, ChaCha), asymmetric (RSA, ECC, EdDSA), hashes (SHA-2/3, BLAKE), ZKP (zk-SNARKs, zk-STARKs, PLONK), homomorphic (BFV, CKKS, TFHE), MPC, post-quantum (lattice: Kyber/Dilithium, hash-based: SPHINCS+), differential privacy, TEEs (SGX, TDX, SEV, Nitro).

---

## Quantum (`Quantum/`)
Qubits, gates (Hadamard, CNOT, T), circuits, Shor's factoring, Grover's search (√N speedup), QFT, teleportation, error correction (surface codes), Hamiltonian simulation, HHL (linear systems), variational (VQE, QAOA).

---

## PhD Frontier (`PhD_Research_Frontier/`)
- **Matrix-Mult exponent ω** — currently ≈ 2.371 (Alman-Williams, Duan et al. 2024).
- **Fastest Shortest-Paths** — almost-linear max-flow (Chen et al. 2022); undirected SSSP (Bernstein et al.).
- **Parameterized Complexity frontiers** — kernelization lower bounds.
- **SETH / ETH** — Strong/Exponential Time Hypothesis; conditional lower bounds.
- **P vs NP approaches** — GCT, natural proofs, algebrization, barrier-avoidance.
- **Algebraic Complexity** — VP vs VNP (algebraic P vs NP).
- **Barriers** — Natural Proofs, Relativization, Algebrization.
- **GCT / Mulmuley** — representation-theoretic attack.
- **Holographic Algorithms** — Valiant; match-gates.
- **Quantum Supremacy** — Sycamore (2019), Jiuzhang, Borealis.
- **Crypto proofs** — VDF, PoW, FHE frontiers.
- **IP = PSPACE**, **MIP* = RE** (Ji et al.).
- **PCP** — short PCPs, quasi-linear length.
- **Hardness of Approximation** — UGC-implied tight bounds.
- **Sum-of-Squares hierarchy** — semidefinite hierarchy for approximation.
- **Planarity Testing in linear time** — Hopcroft-Tarjan, Boyer-Myrvold.
- **Derandomization** — PRGs from circuit lower bounds; Nisan-Wigderson generator.
- **Circuit Lower Bounds frontier** — NEXP ⊄ ACC⁰ (Williams 2011); recent work on depth-3.

---

## Textbooks
- **CLRS** — Intro to Algorithms.
- **Kleinberg-Tardos** — Algorithm Design.
- **Sipser** — Intro to Theory of Computation.
- **Arora-Barak** — Computational Complexity: A Modern Approach (PhD-level).
- **Goldreich** — Computational Complexity: A Conceptual Perspective.
- **Papadimitriou** — Computational Complexity (classic).
- **Tanenbaum** — Modern OS / Networks.
- **Silberschatz** — Database System Concepts.
- **Hennessy-Patterson** — Computer Architecture.
- **Dragon Book** — Compilers.
