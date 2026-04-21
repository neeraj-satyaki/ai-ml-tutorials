"""VAE: encoder outputs mu, logvar; sample z via reparam trick; KL + recon loss."""
import torch
import torch.nn as nn
import torch.nn.functional as F

class VAE(nn.Module):
    def __init__(self, d=784, z=20):
        super().__init__()
        self.fc1 = nn.Linear(d, 256)
        self.mu = nn.Linear(256, z)
        self.logvar = nn.Linear(256, z)
        self.dec = nn.Sequential(nn.Linear(z, 256), nn.ReLU(),
                                 nn.Linear(256, d), nn.Sigmoid())
    def encode(self, x):
        h = F.relu(self.fc1(x))
        return self.mu(h), self.logvar(h)
    def reparam(self, mu, logvar):
        std = (0.5 * logvar).exp()
        return mu + std * torch.randn_like(std)
    def forward(self, x):
        mu, lv = self.encode(x)
        z = self.reparam(mu, lv)
        return self.dec(z), mu, lv

def vae_loss(xh, x, mu, lv):
    recon = F.binary_cross_entropy(xh, x, reduction="sum")
    kl = -0.5 * (1 + lv - mu.pow(2) - lv.exp()).sum()
    return recon + kl

x = torch.rand(4, 784)
xh, mu, lv = VAE()(x)
print("loss:", vae_loss(xh, x, mu, lv).item())
