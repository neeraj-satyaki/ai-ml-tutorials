"""BERT: bidirectional encoder pretrained with masked-LM objective.

Needs: pip install transformers torch
"""
from transformers import AutoTokenizer, AutoModel
import torch

tok = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tok("Hello transformer world", return_tensors="pt")
with torch.no_grad():
    out = model(**inputs)
print("last hidden shape:", out.last_hidden_state.shape)  # (1, seq, 768)
print("pooled [CLS] shape:", out.pooler_output.shape)     # (1, 768)
