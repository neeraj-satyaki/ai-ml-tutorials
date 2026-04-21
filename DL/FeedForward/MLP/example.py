"""MLP: stacked fully-connected layers with nonlinearities."""
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, in_dim=784, hidden=128, out_dim=10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, out_dim),
        )
    def forward(self, x):
        return self.net(x)

model = MLP()
x = torch.randn(4, 784)
logits = model(x)
print("logits shape:", logits.shape)  # (4, 10)
print("param count:", sum(p.numel() for p in model.parameters()))
