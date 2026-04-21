"""DQN: neural Q-function + replay buffer + target network.

Architecture shown; full train loop needs gym env. Install: pip install gymnasium
"""
import torch
import torch.nn as nn
from collections import deque
import random

class QNet(nn.Module):
    def __init__(self, state_dim, n_actions):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 64), nn.ReLU(),
            nn.Linear(64, 64), nn.ReLU(),
            nn.Linear(64, n_actions),
        )
    def forward(self, s): return self.net(s)

buf = deque(maxlen=10_000)
q = QNet(4, 2); q_target = QNet(4, 2)
q_target.load_state_dict(q.state_dict())
opt = torch.optim.Adam(q.parameters(), lr=1e-3)

# pseudo-train step
def train_step(batch_size=32, gamma=0.99):
    if len(buf) < batch_size: return
    batch = random.sample(buf, batch_size)
    s, a, r, ns, d = map(torch.tensor, zip(*batch))
    with torch.no_grad():
        target = r + gamma * q_target(ns.float()).max(1)[0] * (1 - d.float())
    pred = q(s.float()).gather(1, a.long().unsqueeze(1)).squeeze()
    loss = ((pred - target) ** 2).mean()
    opt.zero_grad(); loss.backward(); opt.step()

print("DQN scaffolding ready. Fill buf via env.step(action) in CartPole-v1.")
print("test forward:", q(torch.randn(1, 4)).shape)
