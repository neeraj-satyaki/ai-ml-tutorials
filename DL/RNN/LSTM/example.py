"""LSTM: gated RNN (input, forget, output gates + cell state) vs vanishing grads."""
import torch
import torch.nn as nn

lstm = nn.LSTM(input_size=10, hidden_size=32, num_layers=1, batch_first=True)
x = torch.randn(4, 7, 10)
out, (h, c) = lstm(x)
print("out:", out.shape, "h:", h.shape, "c:", c.shape)
