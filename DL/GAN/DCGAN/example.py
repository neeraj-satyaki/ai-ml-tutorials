"""DCGAN: G (noise -> image) vs D (real/fake). Convolutional. Adversarial loss."""
import torch
import torch.nn as nn

class G(nn.Module):
    def __init__(self, z=100):
        super().__init__()
        self.net = nn.Sequential(
            nn.ConvTranspose2d(z, 128, 4, 1, 0), nn.BatchNorm2d(128), nn.ReLU(),
            nn.ConvTranspose2d(128, 64, 4, 2, 1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, 2, 1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.ConvTranspose2d(32, 1, 4, 2, 1), nn.Tanh(),
        )
    def forward(self, z): return self.net(z)

class D(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 32, 4, 2, 1), nn.LeakyReLU(0.2),
            nn.Conv2d(32, 64, 4, 2, 1), nn.BatchNorm2d(64), nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 4, 2, 1), nn.BatchNorm2d(128), nn.LeakyReLU(0.2),
            nn.Conv2d(128, 1, 4, 1, 0), nn.Sigmoid(),
        )
    def forward(self, x): return self.net(x).view(-1)

z = torch.randn(4, 100, 1, 1)
fake = G()(z)
print("generated:", fake.shape)            # (4, 1, 32, 32)
print("D(fake):", D()(fake).shape)         # (4,)
