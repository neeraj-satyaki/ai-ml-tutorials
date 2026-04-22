# Blockchain + Web3

Beyond `Cybersecurity/Blockchain_Web3_Security/`. Full developer stack.

## Fundamentals
- Hash functions, Merkle trees, digital signatures (ECDSA, Schnorr, BLS).
- **UTXO** (Bitcoin) vs **account model** (Ethereum).
- HD wallets (BIP32/39/44), mnemonic phrases.
- Node types: full, light, archive. Client diversity.

## Consensus
PoW, PoS, DPoS. PBFT, Tendermint / CometBFT, HotStuff. Nakamoto consensus. Casper FFG, **Gasper** (Ethereum post-Merge). Avalanche Snowman. **Narwhal/Bullshark** (Sui, Aptos). DAG protocols (IOTA, Hedera).

## Ethereum stack
- **EVM** opcodes, gas.
- **Solidity**, Vyper, Yul assembly.
- Tooling: **Hardhat**, **Foundry** + Anvil, OpenZeppelin contracts.
- Standards: ERC-20, 721, 1155, 4626 vaults, **ERC-4337 Account Abstraction**.
- EIP-1559 gas, EIP-4844 blobs.
- **Beacon chain** + validators.
- **Rollups**:
  - Optimistic: Arbitrum, Optimism, Base.
  - ZK: zkSync Era, Starknet, Polygon zkEVM, Scroll, Linea.
- **Data availability**: Celestia, EigenDA, Avail, alt-DA.
- **MEV**: Flashbots, MEV-Boost, searchers, builders.
- **Restaking**: EigenLayer, AVS.
- Shared sequencers (Espresso, Astria).

## Other chains (`OtherChains/`)
- **Solana** (Anchor, Sealevel runtime, parallel execution).
- **NEAR** (Rust contracts).
- **Sui / Aptos** (Move language).
- **Cosmos SDK + IBC**.
- **Polkadot / Substrate + XCM**.
- **Cardano** (Plutus, Haskell).
- **Avalanche subnets**.
- **Bitcoin**: Taproot, Ordinals, Inscriptions, Runes, BitVM.
- **Stellar / Soroban**.

## DeFi primitives (`DeFi_Primitives/`)
- AMMs: CPMM (Uniswap v2), CLMM (Uniswap v3/v4), StableSwap.
- Lending: Compound, Aave.
- Stablecoins: overcollateralized (DAI), algorithmic (failed — UST), CDP.
- Perp DEXs: GMX, dYdX, Hyperliquid.
- Oracles: Chainlink, Pyth, UMA.
- Bridges + trust models.
- Liquid staking: Lido, Rocket Pool, EtherFi.
- Account Abstraction (ERC-4337 bundlers + paymasters).

## Tooling (`Tooling/`)
- Client libs: **ethers.js v6**, **viem**, web3.py, web3j.
- Wallet integration: WalletConnect, RainbowKit, Web3Modal, Dynamic.
- **The Graph** subgraphs.
- Storage: IPFS, Arweave, Filecoin, Irys.
- Identity + data: Ceramic, Lit Protocol.
- Analytics: Dune, Flipside, Nansen.
- Testing: Foundry invariant + fuzz, echidna, Medusa.
- Debugging: Tenderly.

## Security (`Security/`)
- Static: **Slither**, Mythril, Echidna, Medusa.
- Formal: **Certora**, **Halmos**, **Kontrol**, hevm.
- Audit checklists.
- Bug bounties: **Immunefi**, Code4rena, **Sherlock**, Cantina.

## ZK (`ZK/`)
SNARKs (Groth16, PlonK, Halo2), STARKs. **zkVMs**: RISC Zero, SP1, Jolt, Nexus. Circom, Noir, Halo2, Arkworks. Privacy: Aztec, Railgun. Account recovery with ZK.

## Books + refs
- *Mastering Ethereum* — Antonopoulos & Wood.
- *Programming Bitcoin* — Song.
- *The Anthology of Auditing* (Spearbit).
- Paradigm, a16z crypto, Flashbots research.
- Solidity docs, Foundry book (`book.getfoundry.sh`).
