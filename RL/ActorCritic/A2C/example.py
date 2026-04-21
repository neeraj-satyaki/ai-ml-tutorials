"""A2C: synchronous advantage actor-critic. Critic V(s) reduces variance of PG."""
import torch
import torch.nn as nn

class AC(nn.Module):
    def __init__(self, s, a):
        super().__init__()
        self.body = nn.Sequential(nn.Linear(s, 64), nn.ReLU())
        self.pi = nn.Linear(64, a)
        self.v = nn.Linear(64, 1)
    def forward(self, s):
        h = self.body(s)
        return torch.distributions.Categorical(logits=self.pi(h)), self.v(h).squeeze(-1)

net = AC(4, 2)
opt = torch.optim.Adam(net.parameters(), lr=1e-3)

s = torch.randn(16, 4)
a = torch.randint(0, 2, (16,))
R = torch.randn(16)                    # n-step returns
dist, v = net(s)
adv = R - v.detach()
loss = -(dist.log_prob(a) * adv).mean() + 0.5 * (R - v).pow(2).mean()
opt.zero_grad(); loss.backward(); opt.step()
print("A2C step loss:", loss.item())
