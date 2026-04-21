# Reinforcement Learning

Agent interacts with environment → maximizes cumulative reward. MDP: (S, A, P, R, γ).

## Value-Based (`ValueBased/`)
Learn value function; derive policy by argmax.
- **QLearning** — off-policy TD; bootstrapped max.
- **SARSA** — on-policy TD; uses actual next action.
- **DQN** — neural Q + replay buffer + target network.
  - Extensions: Double DQN, Dueling DQN, Prioritized Replay, Rainbow.

## Policy-Based (`PolicyBased/`)
Parameterize π_θ; gradient ascent on expected return.
- **REINFORCE** — Monte Carlo policy gradient.
- **PPO** — clipped surrogate; the practical default.
- **TRPO** — trust-region KL constraint + CG.

## Actor-Critic (`ActorCritic/`)
Policy (actor) + value fn (critic) to reduce variance.
- **A2C** — synchronous advantage actor-critic.
- **A3C** — asynchronous workers.
- **DDPG** — deterministic policy, continuous actions, replay.
- **SAC** — stochastic + max-entropy + twin Q; SOTA continuous control.
- **TD3** — DDPG + twin Q + delayed updates + target smoothing.

## Model-Based (`ModelBased/`)
Learn or use environment model; plan.
- **DynaQ** — Q-learning + simulated steps from learned model.
- **MCTS** — tree search (UCT). Core of AlphaGo, AlphaZero, MuZero.

## Multi-Agent (`MultiAgent/`)
- **MADDPG** — per-agent actor (local obs) + centralized critic (global).

---

## Related algorithm families (not in folders)
- **PolicyIteration / ValueIteration** — classical DP given model.
- **Offline RL** — CQL, IQL, AWAC; learn from fixed dataset.
- **Imitation / Behavior Cloning** — learn from expert demos.
- **Inverse RL** — recover reward from behavior (MaxEnt IRL, GAIL).
- **Hierarchical RL** — options, feudal nets.
- **Meta RL** — RL² , PEARL.
- **Exploration** — ε-greedy, UCB, count-based (RND, ICM curiosity).
- **RLHF / RLAIF** — for LLMs: reward from human/AI preferences. Used with PPO, or direct methods (DPO, GRPO, IPO).
- **AlphaZero / MuZero** — MCTS + self-play + learned model.
- **World Models** — Dreamer v1/v2/v3; learn latent dynamics, plan in imagination.

---

## Typical flow
1. Define MDP / POMDP. Design reward (or use RLHF).
2. Pick algo: discrete actions → DQN/PPO; continuous → SAC/PPO.
3. Handle exploration, reward shaping, credit assignment.
4. Evaluate: return, success rate, safety, sample efficiency.
