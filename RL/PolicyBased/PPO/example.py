"""PPO: clipped surrogate objective prevents too-large policy updates.

L = E[ min(r_t A_t, clip(r_t, 1-eps, 1+eps) A_t) ]
"""
import torch
import torch.nn as nn

class ActorCritic(nn.Module):
    def __init__(self, s, a):
        super().__init__()
        self.body = nn.Sequential(nn.Linear(s, 64), nn.Tanh(), nn.Linear(64, 64), nn.Tanh())
        self.pi = nn.Linear(64, a)
        self.v = nn.Linear(64, 1)
    def forward(self, s):
        h = self.body(s)
        return torch.distributions.Categorical(logits=self.pi(h)), self.v(h).squeeze(-1)

net = ActorCritic(4, 2)
opt = torch.optim.Adam(net.parameters(), lr=3e-4)
clip = 0.2

# toy batch
s = torch.randn(64, 4)
a = torch.randint(0, 2, (64,))
adv = torch.randn(64)
ret = torch.randn(64)
with torch.no_grad():
    old_dist, _ = net(s)
    old_logp = old_dist.log_prob(a)

for _ in range(4):                     # multiple epochs of SGD on same batch
    dist, v = net(s)
    logp = dist.log_prob(a)
    ratio = (logp - old_logp).exp()
    clipped = torch.clamp(ratio, 1 - clip, 1 + clip) * adv
    loss_pi = -torch.min(ratio * adv, clipped).mean()
    loss_v = ((v - ret) ** 2).mean()
    loss = loss_pi + 0.5 * loss_v - 0.01 * dist.entropy().mean()
    opt.zero_grad(); loss.backward(); opt.step()
print("PPO update done. final loss:", loss.item())
