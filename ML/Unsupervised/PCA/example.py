"""PCA: linear projection onto axes of maximum variance."""
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X, _ = load_iris(return_X_y=True)
pca = PCA(n_components=2).fit(X)
print("explained variance ratio:", pca.explained_variance_ratio_.round(3))
print("reduced shape:", pca.transform(X).shape)
