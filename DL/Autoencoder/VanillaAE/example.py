"""Autoencoder: compress x -> z -> x_hat. Bottleneck forces learned code."""
import torch
import torch.nn as nn

class AE(nn.Module):
    def __init__(self, d=784, z=32):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(d, 128), nn.ReLU(), nn.Linear(128, z))
        self.dec = nn.Sequential(nn.Linear(z, 128), nn.ReLU(), nn.Linear(128, d), nn.Sigmoid())
    def forward(self, x):
        z = self.enc(x)
        return self.dec(z), z

model = AE()
x = torch.rand(4, 784)
x_hat, z = model(x)
print("recon:", x_hat.shape, "latent:", z.shape)
print("recon MSE:", nn.functional.mse_loss(x_hat, x).item())
