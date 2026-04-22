# Rivermax — NVIDIA Low-Latency Media & Streaming I/O SDK

Rivermax is NVIDIA's **SMPTE ST 2110 + RoCE + RDMA** network I/O library for uncompressed media and high-rate streaming data. Moves packets directly between NIC and GPU memory, bypassing the kernel. Closed-source library; runs on ConnectX-5/6/7, BlueField DPU, Spectrum switches.

---

## Why it exists

Traditional kernel UDP / POSIX sockets cannot sustain 25/100/200 Gb/s uncompressed video with < 10 µs jitter. Rivermax provides:

- **Zero-copy DMA** NIC → GPU (GPUDirect RDMA) or NIC → CPU.
- **Precise TX scheduling** down to sub-µs (PTP-synced).
- **Line-rate RX** at 100-200 Gb/s with correct pacing.
- **SMPTE 2110 / AES67 / TR-03 / RIST** pacing built-in.
- **Kernel bypass** via RDMA verbs-like API.

---

## Target workloads

| Workload | Rivermax role |
|----------|---------------|
| Broadcast production (live TV, sports, venues) | ST 2110-20/-30/-40 send/receive |
| Medical imaging (ultrasound, endoscopy) | uncompressed 4K video ingest |
| High-frequency trading / telemetry | paced, deterministic UDP |
| AI training ingest from many cameras | direct-to-GPU frames |
| 5G fronthaul / vRAN | eCPRI / fronthaul streams |
| Cloud XR / remote rendering | low-jitter streams to/from GPU |

---

## Key primitives

- **Input stream (RX)** — parse incoming flow (IP+UDP+RTP), place payloads directly into GPU/CPU buffers.
- **Output stream (TX)** — schedule packet release times with hardware timestamps.
- **Media sender/receiver** — higher-level ST 2110 video/audio/ANC helpers.
- **Generic stream** — for custom UDP protocols (telemetry, market data, custom broadcast).
- **PTP time source** — IEEE 1588 hardware clock on ConnectX.
- **Packet pacing engine** — per-stream rate + burst control.

---

## Integration surface

- **Holoscan SDK** (NVIDIA medical/edge AI) uses Rivermax under its video/network operators.
- **DeepStream 7+** supports Rivermax input for ultra-low-latency RTP sources.
- **GStreamer** operators (`rivermaxsrc`, `rivermaxsink`).
- **FFmpeg** muxer/demuxer (NVIDIA maintains a fork).
- **Riva / Maxine / Magnum IO** ecosystem.
- **BlueField DPU** offload — pacing + parsing runs on NIC ARM cores.

---

## Minimum system

- Mellanox/NVIDIA ConnectX-5/6/7 or BlueField-2/3.
- NVIDIA driver + MLNX_OFED or DOCA.
- Linux (RHEL/Ubuntu) or Windows.
- PTP grandmaster in network for media workloads.
- Rivermax license (free for dev; paid tier for production in some SKUs).

---

## Example — high-level flow

```
camera --ST 2110 IP--> ConnectX NIC --GPUDirect--> GPU buffer
                                                   |
                                                   v
                                           DeepStream / Holoscan inference
                                                   |
                                                   v
                              ConnectX TX --ST 2110-- back to switcher/monitor
```

All within the same host, no kernel copy, jitter < 10 µs on tuned setup.

---

## Choice vs alternatives

| Need | Use |
|------|-----|
| Low-latency uncompressed broadcast | **Rivermax** |
| General RDMA for compute | libibverbs / UCX |
| Kernel-bypass for custom apps | **DPDK**, AF_XDP |
| Open-source SMPTE 2110 (no NVIDIA NIC) | Nmos / ossrf, libst2110 |
| WebRTC real-time | Pion, LiveKit, mediasoup |
| Cloud-native video pipelines | GStreamer + SRT/RTP |

**Rule of thumb:** Rivermax only if you need ST 2110 compliance OR jitter < 50 µs AND you have NVIDIA NICs. Otherwise DPDK / UCX / GStreamer.

---

## Performance notes

- CPU governor → performance; isolate cores for RX threads.
- HugePages for receive buffers.
- One core per receive flow; interrupt pinning.
- PTP hardware clock disciplined to an external grandmaster, not software NTP.
- Check `ibv_devinfo`, `ethtool -S`, `mlxlink`, `mlnx_tune` for tuning.

---

## Security / Ops considerations

- SMPTE 2110 networks are typically **private, isolated, PTP-enabled fabrics** — not shared with production LAN.
- ACLs at the switch; IGMPv3 SSM for multicast source filtering.
- Backup paths per SMPTE ST 2022-7 (seamless protection).
- Observability: pcap via mirror port, NIC counters (dropped, malformed), Rivermax stats API.

---

## Relation to this repo

- Fits under `DL/ComputerVision/Streaming.md` (ingest section) — Rivermax joins FFmpeg / GStreamer / DeepStream as a lowest-latency ingest path.
- Fits under `ElectronicsCommunication_Embedded/CommunicationSystems/` (transport).
- Fits under `SystemDesign/Networking/` (RDMA + pacing).
- Adjacent to `_REFERENCE/RAPIDS.md` (both NVIDIA, same end-to-end data path from NIC → GPU).

---

## Refs
- developer.nvidia.com/networking/rivermax
- NVIDIA Holoscan SDK docs.
- SMPTE ST 2110 spec family.
- DeepStream Rivermax plugin docs.
