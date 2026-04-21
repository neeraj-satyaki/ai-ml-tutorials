# Computer Architecture

How CPUs and the machine underneath actually work.

## Fundamentals
Instruction cycle, RISC vs CISC, register file, datapath, control unit, endianness, word size, addressing modes.

## ISA-Specifics
x86-64, ARMv8/v9, RISC-V, MIPS, POWER, SPARC. SIMD extensions: SSE/AVX/AVX-512, NEON, SVE.

## Pipelining
5-stage (IF/ID/EX/MEM/WB). Hazards: data, control, structural. Forwarding, stalls, branch prediction (static/dynamic, TAGE), speculative execution, out-of-order (Tomasulo), register renaming, reorder buffer, superscalar, VLIW, super-pipelining.

## Memory
Cache hierarchy L1/L2/L3; coherence (MESI/MOESI). Write-back vs write-through. Associativity; replacement (LRU/PLRU/random). TLB, virtual memory (paging/segmentation), huge pages, HW + SW prefetching, NUMA, memory barriers. Consistency models (SC, TSO, PSO, RC, weak).

## Parallelism
ILP, DLP (SIMD/SIMT), TLP, multicore, SMT/hyperthreading, GPU streaming multiprocessors, tensor cores, matrix engines, systolic arrays (TPU), dataflow, neuromorphic, processing-in-memory (PIM).

## Interconnect / I/O
PCIe, NVLink, CXL, InfiniBand, RDMA Ethernet, UCIe chiplets. NVMe. DMA, MSI-X interrupts, IOMMU, SR-IOV.

## Power / Reliability
DVFS, C/P states, thermal design, ECC memory, RAS, soft errors, radiation hardening, clock gating.

## Security
Meltdown/Spectre, side channels, ROP, CET, pointer authentication, memory tagging (MTE), TEEs (SGX/TDX/SEV/CCA/Keystone), TrustZone, secure boot, firmware verification.

## Classic books
- *Computer Architecture: A Quantitative Approach* — Hennessy & Patterson.
- *Computer Organization and Design* — Patterson & Hennessy.
- *What Every Programmer Should Know About Memory* — Ulrich Drepper.
