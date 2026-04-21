"""REINFORCE: Monte Carlo policy gradient. L = -E[ log pi(a|s) * G_t ]."""
import torch
import torch.nn as nn

class Policy(nn.Module):
    def __init__(self, s, a):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(s, 64), nn.ReLU(), nn.Linear(64, a))
    def forward(self, s):
        return torch.distributions.Categorical(logits=self.net(s))

pi = Policy(4, 2)
opt = torch.optim.Adam(pi.parameters(), lr=1e-3)

# one-episode pseudo-update with fake rollout
states = torch.randn(20, 4)
actions = torch.randint(0, 2, (20,))
rewards = torch.ones(20)              # would be env rewards
returns = torch.flip(torch.cumsum(torch.flip(rewards, [0]), 0), [0])
returns = (returns - returns.mean()) / (returns.std() + 1e-8)

dist = pi(states)
logp = dist.log_prob(actions)
loss = -(logp * returns).mean()
opt.zero_grad(); loss.backward(); opt.step()
print("REINFORCE step loss:", loss.item())
