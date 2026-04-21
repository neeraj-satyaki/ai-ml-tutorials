# Operating Systems

OS = resource multiplexer + abstraction layer.

## Processes + Threads
PCB, context switch, fork/exec/wait, thread models (user/kernel, M:N), coroutines/fibers, async runtimes.

## Scheduling
FCFS, SJF, Priority, RR, MLFQ. Linux CFS → EEVDF (2023). Realtime: EDF, Rate-Monotonic. SMP load balancing, CPU affinity, IRQ handling.

## Synchronization
Mutex, semaphore, monitor, condvar, spinlock, RCU, atomic/CAS, memory barriers, deadlock detect/avoidance, livelock, priority inversion.

## Memory
Address spaces, paging, segmentation, TLB, demand paging, COW, page replacement (LRU/clock/aging/working-set), swap, anonymous vs file-backed, slab/buddy allocators (jemalloc/tcmalloc), overcommit/OOM killer, transparent huge pages.

## File Systems
VFS abstraction. ext2/3/4, XFS, Btrfs, ZFS, F2FS, NTFS, APFS, FAT32/exFAT, NFS, SMB/CIFS, Ceph, GlusterFS, FUSE. Inodes, journaling, COW FS, encryption (LUKS/fscrypt).

## I/O
Device drivers (char/block/network), block layer, I/O schedulers (CFQ, deadline, BFQ), async I/O (io_uring, aio), polling/interrupt/DMA, USB stack, SCSI/AHCI/NVMe.

## Networking Stack
Sockets, kernel TCP/IP, namespaces, BPF/eBPF, XDP, netfilter/iptables/nftables, traffic control (qdisc), RDMA.

## Virtualization
Type 1 vs 2 hypervisors. KVM, QEMU, Xen. Containers (namespaces + cgroups). OverlayFS. Kata, Firecracker, gVisor. WASM sandboxes. systemd resource control.

## Security
DAC, capabilities, LSMs (SELinux/AppArmor), seccomp-bpf, TPM, measured/secure boot (UEFI), auditd, IMA/EVM, rootkit detection.

## Realtime / Embedded
FreeRTOS, Zephyr, QNX, VxWorks. PREEMPT_RT Linux. Hard vs soft realtime. Latency bounds. Tickless kernel.

## Books
- *Operating Systems: Three Easy Pieces* (OSTEP) — Remzi & Andrea Arpaci-Dusseau (free, PhD-level free resource).
- *Modern Operating Systems* — Tanenbaum.
- *Linux Kernel Development* — Love.
- *Understanding the Linux Kernel* — Bovet & Cesati.
