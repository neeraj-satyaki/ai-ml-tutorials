"""DDPG: deterministic policy gradient for continuous actions + target nets + replay."""
import torch
import torch.nn as nn

class Actor(nn.Module):
    def __init__(self, s, a, a_max=1.0):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(s, 64), nn.ReLU(),
                                 nn.Linear(64, a), nn.Tanh())
        self.a_max = a_max
    def forward(self, s): return self.a_max * self.net(s)

class Critic(nn.Module):
    def __init__(self, s, a):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(s + a, 64), nn.ReLU(),
                                 nn.Linear(64, 1))
    def forward(self, s, a): return self.net(torch.cat([s, a], -1)).squeeze(-1)

actor, critic = Actor(3, 1), Critic(3, 1)
print("actor(s):", actor(torch.randn(2, 3)).shape)
print("critic(s,a):", critic(torch.randn(2, 3), torch.randn(2, 1)).shape)
print("Train: soft-update target nets; Q target = r + gamma * Q_t(s', pi_t(s'))")
