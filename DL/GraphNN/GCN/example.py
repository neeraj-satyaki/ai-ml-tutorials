"""GCN: H' = sigma(A_hat H W). Node features aggregated from neighbors."""
import torch
import torch.nn as nn

def normalize_adj(A):
    A = A + torch.eye(A.size(0))
    d = A.sum(1)
    D_inv_sqrt = torch.diag(d.pow(-0.5))
    return D_inv_sqrt @ A @ D_inv_sqrt

class GCNLayer(nn.Module):
    def __init__(self, in_f, out_f):
        super().__init__()
        self.lin = nn.Linear(in_f, out_f)
    def forward(self, x, A_hat):
        return torch.relu(A_hat @ self.lin(x))

# toy graph: 4 nodes, ring
A = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], dtype=torch.float)
A_hat = normalize_adj(A)
X = torch.randn(4, 8)

gcn = nn.Sequential()
layer1, layer2 = GCNLayer(8, 16), GCNLayer(16, 2)
h = layer2(layer1(X, A_hat), A_hat)
print("node embeddings:", h.shape)  # (4, 2)
