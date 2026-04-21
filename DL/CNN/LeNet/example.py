"""LeNet-5: classic CNN (conv-pool-conv-pool-fc) for digit images."""
import torch
import torch.nn as nn

class LeNet(nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 6, 5, padding=2), nn.ReLU(), nn.AvgPool2d(2),
            nn.Conv2d(6, 16, 5), nn.ReLU(), nn.AvgPool2d(2),
        )
        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Linear(16 * 5 * 5, 120), nn.ReLU(),
            nn.Linear(120, 84), nn.ReLU(),
            nn.Linear(84, n_classes),
        )
    def forward(self, x):
        return self.head(self.features(x))

model = LeNet()
x = torch.randn(2, 1, 28, 28)
print("output shape:", model(x).shape)  # (2, 10)
