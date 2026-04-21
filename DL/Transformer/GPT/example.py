"""GPT-style: causal (masked) self-attention decoder. Toy mini-GPT block."""
import torch
import torch.nn as nn

class CausalSelfAttention(nn.Module):
    def __init__(self, d, h):
        super().__init__()
        self.h, self.d = h, d
        self.qkv = nn.Linear(d, 3 * d)
        self.proj = nn.Linear(d, d)
    def forward(self, x):
        B, T, D = x.shape
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        def split(t): return t.view(B, T, self.h, D // self.h).transpose(1, 2)
        q, k, v = split(q), split(k), split(v)
        att = (q @ k.transpose(-2, -1)) / (D // self.h) ** 0.5
        mask = torch.tril(torch.ones(T, T, device=x.device)).bool()
        att = att.masked_fill(~mask, float("-inf")).softmax(dim=-1)
        y = (att @ v).transpose(1, 2).contiguous().view(B, T, D)
        return self.proj(y)

class Block(nn.Module):
    def __init__(self, d=64, h=4):
        super().__init__()
        self.ln1, self.ln2 = nn.LayerNorm(d), nn.LayerNorm(d)
        self.attn = CausalSelfAttention(d, h)
        self.mlp = nn.Sequential(nn.Linear(d, 4 * d), nn.GELU(), nn.Linear(4 * d, d))
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x

x = torch.randn(2, 10, 64)
print("block output:", Block()(x).shape)
