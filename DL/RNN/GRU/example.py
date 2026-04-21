"""GRU: simpler gated RNN than LSTM (reset + update gates, no cell)."""
import torch
import torch.nn as nn

gru = nn.GRU(input_size=10, hidden_size=32, num_layers=1, batch_first=True)
x = torch.randn(4, 7, 10)
out, h = gru(x)
print("out:", out.shape, "h:", h.shape)
