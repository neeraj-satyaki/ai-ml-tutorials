"""t-SNE: nonlinear 2D embedding preserving local neighborhoods."""
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
Z = TSNE(n_components=2, perplexity=30, random_state=0, init="pca").fit_transform(X[:500])
print("embedded shape:", Z.shape)
print("sample:", Z[:3].round(2))
