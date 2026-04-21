"""Hierarchical clustering: build tree by merging closest clusters (agglomerative)."""
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=200, centers=3, random_state=0)
ac = AgglomerativeClustering(n_clusters=3, linkage="ward").fit(X)
print("labels distribution:", {int(l): int((ac.labels_ == l).sum()) for l in set(ac.labels_)})
