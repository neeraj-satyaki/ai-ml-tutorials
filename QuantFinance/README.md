# Quantitative Finance + HFT Tech

Market structure → strategies → modeling → HFT infra → ML trading → risk/ops.

## Market structure
Exchanges (NYSE, Nasdaq, CME), **Limit Order Book (LOB)** mechanics. Order types (market, limit, stop, IOC, FOK). Matching engines. Tick data L1/L2/L3. Dark pools, PFOF, market makers. **FIX protocol**, Nasdaq ITCH/OUCH. Colocation / proximity hosting.

## Strategies
**Market making**. StatArb / pairs / cointegration. Triangular arb (FX). Index arb. Momentum / trend following. Mean reversion. Fama-French factor investing. Fixed-income relative value. Vol arb (gamma sell). Vol forecasting (GARCH). News alpha (NLP). Alt data (satellite, credit-card). **Crypto MEV** arb. DeltaOne / ETF. Convertible arb. Merger arb.

## Modelling
**Black-Scholes-Merton**, **Heston / SABR** stoch vol, Merton jump-diffusion, Dupire local vol. Interest rates: Hull-White, HJM, LMM. Credit: structural + reduced form. Monte Carlo + QMC. PDE (finite difference). American options (Longstaff-Schwartz). **Greeks** (Δ/Γ/V/Θ). **XVA** (CVA, FVA, MVA). Portfolio opt: Markowitz MVO, Black-Litterman, risk parity, Kelly. **VaR, CVaR, ES**. Stress testing.

## HFT tech
**Kernel bypass** (DPDK, XDP, Onload/Solarflare). **FPGA trading** (Velocore, Xilinx). **ASIC trading** (custom silicon). Low-latency C++ (no-heap, template-heavy). Lock-free ring buffers. Busy polling. **RDMA / InfiniBand**. **PTP** time sync. UDP multicast. Exchange gateways. **SOR** (smart order routing). Internal crossing networks. Tick-to-trade budget (ns → μs). Micro-benchmark cycles.

## ML trading
Feature engineering on time series. **Triple-barrier labeling** (de Prado). **Purged + combinatorial K-fold CV**. Feature importance (MDA, SFI, PFI). Backtesting: VectorBT, Backtrader, **Zipline / QuantConnect Lean**. Walk-forward analysis. Overfitting / sample bias. Regime detection (HMM, BOCPD). RL for order execution (Almgren-Chriss, TradeAll). Deep-learning forecasting (NBEATS, PatchTST, TimesNet). RL trading (DDPG, SAC, PPO). LLM factor extraction from news/filings.

## Risk + Ops
Regulatory capture (MiFID II, Dodd-Frank). Surveillance (layering, spoofing). Circuit breakers. Pre-trade limit checks. Post-trade settlement. CCP clearing. Chinese wall. **SR 11-7 model risk**. WORM audit trail. Multi-DC DR.

## Books
- Hull — *Options, Futures, Other Derivatives*.
- Wilmott — *PWIQF*.
- Joshi — *Concepts + Math. Finance*.
- **Meucci** — *Risk and Asset Allocation*.
- **de Prado** — *Advances in Financial ML*.
- Narang — *Inside the Black Box*.
- Harris — *Trading and Exchanges*.
- Haug — *Complete Guide to Option Pricing*.
