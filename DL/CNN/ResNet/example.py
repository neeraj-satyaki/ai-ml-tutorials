"""ResNet: skip connections let very deep nets train (residual learning)."""
import torch
import torch.nn as nn

class ResBlock(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.conv1 = nn.Conv2d(c, c, 3, padding=1)
        self.conv2 = nn.Conv2d(c, c, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(c)
        self.bn2 = nn.BatchNorm2d(c)
    def forward(self, x):
        h = torch.relu(self.bn1(self.conv1(x)))
        h = self.bn2(self.conv2(h))
        return torch.relu(h + x)            # skip connection

class TinyResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.stem = nn.Conv2d(3, 16, 3, padding=1)
        self.blocks = nn.Sequential(ResBlock(16), ResBlock(16))
        self.head = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(),
                                  nn.Linear(16, 10))
    def forward(self, x):
        return self.head(self.blocks(self.stem(x)))

model = TinyResNet()
print("out:", model(torch.randn(2, 3, 32, 32)).shape)
