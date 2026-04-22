# Quantum Programming

Beyond `CS/Quantum/` theory — developer stack for quantum computation.

## SDKs (`SDKs/`)
- **Qiskit** (IBM) — most mature Python SDK.
- **Cirq** (Google) — research + TPU/NISQ.
- **PennyLane** (Xanadu) — differentiable quantum + PyTorch/JAX interop.
- **Ocean** (D-Wave) — quantum annealing.
- **Q# / MS Quantum Dev Kit**.
- **Amazon Braket** SDK.
- **CUDA-Q** (NVIDIA) — GPU-accelerated hybrid quantum-classical.
- **tket** (Quantinuum).
- **Strawberry Fields** (photonic).

## Algorithms (`Algorithms/`)
- Grover (search), Shor (factoring), QFT, Quantum Phase Estimation.
- **HHL** linear systems.
- Variational: **VQE** (chemistry), **QAOA** (combinatorial opt).
- Quantum ML: **quantum kernels**, variational classifiers.
- Quantum walks, teleportation, superdense coding.
- **QKD**: BB84, E91.

## Error correction (`ErrorCorrection/`)
Surface code, Steane, Bacon-Shor, Reed-Muller, quantum LDPC. Magic state distillation. Decoders: Union-Find, MWPM. **Real-time decoders** — AWS Ocelot + Google AlphaQubit (2024 DeepMind) + Microsoft Majorana 1 (2025).

## Hardware types (`Hardware_Types/`)
- **Superconducting** (IBM, Google, Rigetti) — transmons.
- **Trapped-ion** (IonQ, Quantinuum, Oxford).
- **Photonic** (Xanadu, PsiQuantum).
- **Neutral atoms** (QuEra, Pasqal, Atom Computing).
- **Topological** (Microsoft Majorana 1 — 2025 announcement).
- **Spin in silicon** (Intel, SiQC / Diraq).
- **Annealing** (D-Wave Advantage).

## Compilers / transpilers (`Compilers_Transpilers/`)
**OpenQASM 3**, Qiskit transpiler, Cirq compiler, Staq. Clifford+T gate synthesis. Pulse-level control. CUDA-Q MLIR + QIR.

## Simulation (`Simulation/`)
- **State vector** (up to ~40 qubits).
- **Density matrix** (with noise).
- **Tensor networks** (MPS, PEPS) — far more qubits, limited entanglement.
- **Clifford simulation** — **Stim** (billions of qubits for stabilizer circuits).
- Noise models (Kraus ops).
- **cuQuantum**, PennyLane-Lightning, Qiskit Aer, QuEST, Tequila (chemistry).

## Applications (`ApplicationsDomains/`)
- **Chemistry**: VQE for small molecules, active space methods.
- **Optimization**: QAOA for portfolio, routing, scheduling.
- **QML** classification on NISQ.
- **Cryptanalysis**: Shor threat to RSA/ECC → PQC migration.
- **Finance**: Monte Carlo, option pricing.
- **Drug discovery**, materials design.
- **Sensing**: quantum magnetometers, atomic clocks.

## Practical advice
- 2025 state: NISQ regime. Useful for research + select HPC augmentation.
- Real applications use **hybrid quantum-classical** (variational).
- Expect real fault-tolerant advantage in 2028-2032 range (industry forecasts).
- Learn Qiskit first, then venture into CUDA-Q / Stim / PennyLane.

## Books + refs
- *Quantum Computation and Quantum Information* — Nielsen & Chuang (bible).
- *Quantum Computing: An Applied Approach* — Hidary.
- *Programming Quantum Computers* — Johnston, Harrigan, Gimeno-Segovia.
- Qiskit textbook (free).
- PennyLane demos.
- Scott Aaronson's blog + lecture notes.
