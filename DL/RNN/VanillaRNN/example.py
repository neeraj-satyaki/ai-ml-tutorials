"""Vanilla RNN: h_t = tanh(W_x x_t + W_h h_{t-1} + b)."""
import torch
import torch.nn as nn

rnn = nn.RNN(input_size=10, hidden_size=32, num_layers=1, batch_first=True)
x = torch.randn(4, 7, 10)           # (batch, seq, feat)
out, h = rnn(x)
print("out:", out.shape, "h:", h.shape)
