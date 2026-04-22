# Mellanox → NVIDIA Networking Stack

Mellanox = NIC + switch + fabric vendor. NVIDIA acquired 2020 ($7B). Now branded "NVIDIA Networking". Backbone of most AI training clusters + HFT + HPC + broadcast.

---

## 1. Product pillars

### NICs — ConnectX series
Ethernet + InfiniBand, programmable, hardware offloads.
- **ConnectX-5** (2017) — 100 Gb/s, RoCEv2, GPUDirect RDMA.
- **ConnectX-6 Dx / Lx** — 200 Gb/s, IPsec offload, TLS inline crypto.
- **ConnectX-7** (2021) — 400 Gb/s, NDR InfiniBand.
- **ConnectX-8** (2024) — 800 Gb/s, PCIe Gen6, CXL, compute-enhanced.

### DPUs — BlueField
Full SoC on a NIC. ARM cores + NIC + accelerators.
- **BlueField-2** (2020) — 8× Cortex-A72, 200 Gb/s, storage + sec offload.
- **BlueField-3** (2023) — 16× Cortex-A78, 400 Gb/s, programmable DOCA.
- **BlueField-4** (announced) — even more compute, integrated with GPU fabrics.
- Use cases: isolate tenant networking, offload OVS/firewall/TLS/telemetry from host CPU, bare-metal clouds, zero-trust infra.

### Switches — Spectrum (Ethernet) + Quantum (InfiniBand)
- **Spectrum-4** — 51.2 Tb/s Ethernet ASIC, 800 GbE ports.
- **Quantum-2** — NDR (400 Gb/s) InfiniBand.
- **Quantum-X800** (2024) — XDR InfiniBand (800 Gb/s), optimized for AI pods.
- Features: SHARPv3 in-network reductions, congestion control (adaptive routing), telemetry.

### Cables + Optics
LinkX QSFP56/112/224 DAC, AOC, MPO fiber. Critical: transceiver compatibility dictates lab/purchase decisions.

---

## 2. Software stack

### MLNX_OFED / DOCA-OFED
Driver + user-space libs for RDMA, verbs, DPDK, SR-IOV. Backward-compat package.

### DOCA SDK
2021+; unified for BlueField DPUs. Libraries: `doca-flow`, `doca-comm-channel`, `doca-telemetry`, `doca-urom`. Reference apps: firewall, IPS, storage.

### UCX
Unified Communication X — transport abstraction on top of RDMA, CUDA, TCP. Used by MPI implementations + NCCL under the hood.

### SHARP (Scalable Hierarchical Aggregation and Reduction Protocol)
In-network compute. Switches perform reduction operations (sum/max/min) on the fly. Cuts all-reduce latency ~2-3x in DL training on InfiniBand fabrics.

### UFM (Unified Fabric Manager)
Management + telemetry platform for InfiniBand fabrics. Topology, congestion, RDMA counters, ML-based anomaly detection.

### Cumulus Linux
Acquired with Mellanox. Open switch OS (Debian-based). Industry-standard on Spectrum hardware.

---

## 3. Transport modes

| Mode | Path |
|------|------|
| **RoCEv2** | RDMA over Ethernet (UDP-encap). Lossless via PFC / DCB. |
| **InfiniBand (Verbs)** | native RDMA, lossless by design. |
| **TCP** | standard kernel stack. |
| **DPDK** | user-space poll-mode driver, kernel bypass. |
| **XDP / AF_XDP** | kernel-bypass via BPF. |
| **VMA / libvma** | Mellanox socket acceleration. |
| **OpenOnload-equivalent** | commercial alternative on Solarflare (now AMD); Mellanox uses VMA / UCX. |
| **GPUDirect RDMA** | NIC → GPU memory direct (no host bounce). |
| **GPUDirect Storage** | NIC → GPU direct from NVMe. |
| **NVSHMEM over InfiniBand** | GPU-to-GPU symmetric memory across nodes. |

---

## 4. Where they sit in AI clusters

- **NCCL** over NVLink intra-node + InfiniBand inter-node. Mellanox NICs + Quantum switches are the default reference for DGX/HGX.
- **Ring / Tree / 2D all-reduce** choose fabric-aware.
- **SHARP** offloads the reduction to switches → fewer hops for gradient sync.
- **GPUDirect RDMA** + **GPUDirect Storage** eliminate CPU-memory copies in training.
- **NIM / Triton** inference benefits from low-latency fabric for multi-node serving.

---

## 5. HFT + finance use

- ConnectX with **VMA** or custom kernel-bypass for market data + order entry.
- Hardware timestamping (PTP, PPS).
- **BlueField** for colocation — per-tenant network isolation + microsecond firewall.
- Competitors: Xilinx Alveo (AMD FPGA), Intel E810 + DPDK, Solarflare/AMD.

---

## 6. Broadcast / media use

- ConnectX-6/7 are the canonical NICs for **Rivermax + SMPTE 2110** fabrics.
- Spectrum + NetQ for broadcast IP networks.
- See `_REFERENCE/Rivermax.md` for API layer.

---

## 7. Cloud / tenant networking

- BlueField DPUs run VPC / VNI / overlays off-host.
- AWS Nitro, Azure Boost, and Google IPU are analogs — Mellanox/BlueField is the OEM path for private/sovereign clouds to do the same.
- Snap (`SmartNIC NVMe virtualization`) exposes a fake NVMe device backed by remote storage.

---

## 8. Telemetry + observability

- **WJH (What Just Happened)** — flow-level drop analytics on Spectrum.
- `nvnet-exporter` + Prometheus.
- **UFM** fabric monitoring.
- `ethtool -S` extended counters.
- Packet captures: switch span ports + ConnectX hairpin.

---

## 9. Typical deployments

| Scenario | Hardware |
|----------|----------|
| DGX H100/H200/B200 training pod | ConnectX-7/8 + Quantum-2 / Quantum-X800 InfiniBand |
| HPC cluster (weather, physics) | ConnectX + Quantum, UCX+MPI |
| Hyperscale Ethernet AI pod | ConnectX + Spectrum-4, RoCEv2 + SHARP |
| HFT colo | ConnectX-6 Dx + VMA + hardware timestamps |
| Broadcast facility | ConnectX + Spectrum + Rivermax |
| Zero-trust bare-metal cloud | BlueField-3 + DOCA |
| Storage fabric | ConnectX + NVMe-oF over RoCE or IB |

---

## 10. Competitors

- **Intel** E810 (ICE), IPU (Mount Evans). Decent, behind in AI fabrics.
- **Broadcom** Thor (NIC), Tomahawk + Jericho (switches). Big in hyperscale Ethernet.
- **AMD/Pensando** DPU (Distributed Services Card). Oracle partnership.
- **Marvell** OCTEON DPUs.
- **Cisco** Silicon One (AI switching push, 2023+).
- **Arista** (switches + CloudVision) — plays both with Broadcom + Mellanox.

---

## 11. Learning path

1. Install MLNX_OFED / DOCA-OFED on a test box; run `ibv_devinfo`, `ibstat`.
2. Read verbs tutorial → write a minimal RDMA send/recv.
3. Set up two machines, benchmark with `ib_write_bw` and `qperf`.
4. Enable RoCEv2 on Ethernet, enable PFC, test lossless.
5. Instrument with `perfquery` and UFM.
6. Explore DOCA samples on BlueField simulator.
7. Tune NCCL over IB: `NCCL_IB_DISABLE=0`, HCA pinning, PXN, SHARP enable.

---

## 12. Relation to this repo

- Binds: `ComputerArchitecture/Interconnect_IO`, `OperatingSystems/Networking_Stack`, `HPC/Communication`, `DL/ComputerVision/Streaming.md`, `_REFERENCE/Rivermax.md`, `QuantFinance/HFT_Tech`, `SystemDesign/Networking`.
- Kernel-bypass + RDMA context for `_REFERENCE/Realtime_IPC_Protocols.md` §8.

---

## Refs
- NVIDIA Networking docs (`docs.nvidia.com/networking`).
- DOCA developer hub.
- UCX project: `openucx.org`.
- InfiniBand Trade Association specs.
- `ibv_*` tutorials.
- "RDMA Aware Networks Programming User Manual" (NVIDIA).
