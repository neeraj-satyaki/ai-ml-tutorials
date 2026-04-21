"""MADDPG: per-agent actor (local obs) + centralized critic (all obs/actions).

Handles non-stationarity of multi-agent RL during training.
"""
import torch
import torch.nn as nn

class Actor(nn.Module):
    def __init__(self, obs_dim, act_dim):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(obs_dim, 64), nn.ReLU(),
                                 nn.Linear(64, act_dim), nn.Tanh())
    def forward(self, o): return self.net(o)

class CentralCritic(nn.Module):
    """Takes ALL agents' observations and actions."""
    def __init__(self, total_obs, total_act):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(total_obs + total_act, 128), nn.ReLU(),
                                 nn.Linear(128, 1))
    def forward(self, all_obs, all_act):
        return self.net(torch.cat([all_obs, all_act], -1)).squeeze(-1)

# 2 agents, each sees 3-dim obs, acts 1-dim
a1, a2 = Actor(3, 1), Actor(3, 1)
critic = CentralCritic(total_obs=6, total_act=2)

o = torch.randn(4, 6)                  # concat of both agents' obs
acts = torch.cat([a1(o[:, :3]), a2(o[:, 3:])], dim=-1)
print("Q(all_o, all_a):", critic(o, acts).shape)
