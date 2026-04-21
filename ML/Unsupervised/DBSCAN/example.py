"""DBSCAN: density-based clustering; no k needed; labels noise as -1."""
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, _ = make_moons(n_samples=300, noise=0.08, random_state=0)
db = DBSCAN(eps=0.2, min_samples=5).fit(X)
n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
print(f"clusters found: {n_clusters}, noise pts: {(db.labels_ == -1).sum()}")
