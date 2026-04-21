"""DDPM: forward = gradual gaussian noise; reverse = learn to denoise.

Shown: forward noising schedule + single reverse step (untrained eps_theta)."""
import torch
import torch.nn as nn

T = 100
betas = torch.linspace(1e-4, 0.02, T)
alphas = 1 - betas
alpha_bar = torch.cumprod(alphas, dim=0)

def q_sample(x0, t, noise):
    """Forward: x_t = sqrt(abar_t) x0 + sqrt(1-abar_t) eps."""
    ab = alpha_bar[t].view(-1, 1)
    return ab.sqrt() * x0 + (1 - ab).sqrt() * noise

# toy eps-predictor: tiny MLP
eps_theta = nn.Sequential(nn.Linear(4, 64), nn.ReLU(), nn.Linear(64, 3))

x0 = torch.randn(8, 3)                  # 3-dim "image"
t = torch.randint(0, T, (8,))
noise = torch.randn_like(x0)
xt = q_sample(x0, t, noise)

t_norm = (t / T).view(-1, 1)
inp = torch.cat([xt, t_norm], dim=1)
pred_noise = eps_theta(inp)
print("xt:", xt.shape, "pred_noise:", pred_noise.shape)
print("loss (untrained):", ((pred_noise - noise) ** 2).mean().item())
