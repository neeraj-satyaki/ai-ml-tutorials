"""K-Means: partition data into k clusters minimizing within-cluster variance."""
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4, random_state=0)
km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(X)
print("centers:\n", km.cluster_centers_.round(2))
print("inertia:", round(km.inertia_, 2))
