# RAPIDS — GPU-accelerated Data Science Stack

NVIDIA's open-source suite for running pandas / scikit-learn / Spark / graph / signal workloads on GPUs with ~10-100x speedups over CPU. Apache-licensed, CUDA-based.

---

## Why it exists

CPU data science tops out on one socket. Datasets are bigger, deadlines shorter. RAPIDS keeps the familiar Python API (pandas, sklearn, networkx, SciPy signal) but runs on GPU via CUDA + Apache Arrow columnar memory. Zero-copy across libraries, zero-copy across GPUs via NVLink + UCX.

---

## Core libraries

| Lib | CPU counterpart | What it does |
|-----|-----------------|--------------|
| **cuDF** | pandas | DataFrames, groupby, joins, I/O (CSV/Parquet/ORC/JSON) |
| **cuML** | scikit-learn | kNN, RF, linear models, tSNE, UMAP, HDBSCAN, PCA, SVM, ARIMA |
| **cuGraph** | NetworkX | PageRank, Louvain, Jaccard, BFS, shortest paths, Leiden |
| **cuSpatial** | GeoPandas | point-in-polygon, trajectories, spatial joins |
| **cuSignal** | scipy.signal | FFT, filters, polyphase resampling, spectrograms |
| **cuxfilter** | crossfilter / bokeh | interactive dashboards on GPU data |
| **RAFT** | — | reusable primitives (ANN search, clustering, solvers) |
| **RMM** | — | RAPIDS Memory Manager — pool/arena allocators |
| **UCX + UCX-Py** | — | GPU-to-GPU transport (RDMA, NVLink, TCP) |
| **Dask-CUDA / Dask-cuDF** | Dask | multi-GPU / multi-node scale-out |
| **cuDF-pandas** | — | zero-code pandas acceleration (2023+, `%load_ext cudf.pandas`) |
| **cuSolver / cuSPARSE** | LAPACK / SciPy sparse | wrapped by cuML |
| **nvTabular** | — | tabular ETL for recsys (Merlin family) |
| **Morpheus** | — | GPU-accelerated cyber / threat-detection pipelines |
| **Clara Parabricks** | — | genomics (BWA, GATK) on GPU |

---

## Integration surface

- **Arrow memory** — zero-copy between cuDF, PyTorch (`.from_dlpack`), TensorFlow, CuPy, Numba.
- **Spark on RAPIDS** — drop-in: `spark.plugins=com.nvidia.spark.SQLPlugin`. SQL + DataFrame ops run on GPU.
- **Dask scheduler** for multi-GPU — same API as Dask.
- **BlazingSQL (legacy)** → merged into cuDF SQL engine.
- **Polars** interop via Arrow.

---

## Ecosystem placement

- **Nvidia Merlin** (recsys): nvTabular + cuDF + HugeCTR + Triton.
- **Nvidia Morpheus** (cybersec): streaming inference for logs/network flows.
- **Nvidia Holoscan** (medical/edge): includes RAPIDS for data prep.
- **DOCA** on BlueField DPUs — offload RAPIDS I/O.

---

## Typical stack upgrades

| From | To (RAPIDS) | Usual speedup |
|------|-------------|---------------|
| pandas 100M-row groupby | cuDF | 20-50x |
| sklearn RF on 10M rows | cuML | 10-40x |
| NetworkX PageRank (1B edges) | cuGraph | 100-500x |
| Spark SQL join | Spark-RAPIDS | 2-10x, better on wide joins |
| ETL for DL train | nvTabular | 5-30x vs pandas prep |

---

## Install

```bash
# Conda (recommended)
conda create -n rapids-24.10 -c rapidsai -c conda-forge -c nvidia \
    rapids=24.10 python=3.11 cuda-version=12.5

# Pip (Linux + CUDA 12)
pip install cudf-cu12 cuml-cu12 cugraph-cu12 \
    --extra-index-url https://pypi.nvidia.com
```

Versioned release cadence: every ~2 months.

---

## Minimal examples

### cuDF drop-in pandas
```python
import cudf
df = cudf.read_parquet("trades.parquet")          # GPU load
big = df[df["notional"] > 1e6].groupby("symbol").agg({"notional": "sum"})
big.to_pandas()                                    # back to host if needed
```

### Zero-code pandas acceleration (2023+)
```python
%load_ext cudf.pandas
import pandas as pd       # now GPU-accelerated where possible
```

### cuML kNN classifier
```python
from cuml.neighbors import KNeighborsClassifier
import cudf
X = cudf.read_parquet("features.parquet"); y = X.pop("label")
clf = KNeighborsClassifier(n_neighbors=15).fit(X, y)
```

### cuGraph PageRank
```python
import cugraph, cudf
edges = cudf.read_csv("edges.csv", names=["src","dst"])
G = cugraph.Graph(); G.from_cudf_edgelist(edges, source="src", destination="dst")
pr = cugraph.pagerank(G)
```

### Multi-GPU with Dask-cuDF
```python
from dask_cuda import LocalCUDACluster
from dask.distributed import Client
import dask_cudf
cluster = LocalCUDACluster(); client = Client(cluster)
ddf = dask_cudf.read_parquet("s3://bucket/data-*.parquet")
ddf.groupby("user").agg({"amount": "sum"}).compute()
```

---

## When to reach for RAPIDS

- Pandas job takes > 60s and fits in GPU memory (≥ 10x expected gain).
- Sklearn training > 5 min and model family is supported by cuML.
- Graph analytics on 10^8+ edges.
- ETL pipeline for GPU-trained model (DL) — keep data on-device end-to-end.
- Spark jobs dominated by shuffle-free transforms, joins, GROUP BY.
- Streaming cybersec / log inspection (Morpheus).

## When NOT to reach for RAPIDS

- Data fits in memory + pandas job under a few seconds.
- Team has no NVIDIA GPUs.
- Code path needs exotic pandas features cuDF hasn't implemented (rare now, still happens).
- Tiny ML model where sklearn is already fast enough.
- You need bit-exact match with sklearn (subtle numerical differences exist).

---

## Relation to this repo
- Speeds up `ML/Unsupervised/KMeans`, `ML/Supervised/RandomForest`, `ML/Streaming/*` feature prep.
- Replaces pandas in `DataScience/Pipeline/FeatureEngineering`.
- Plugs into `Ops/MLOps` training + feature-store pipelines.
- Morpheus belongs under `Cybersecurity/DefensiveSecurity_BlueTeam` + `Ops/SecOps`.

---

## Refs
- docs.rapids.ai
- github.com/rapidsai
- github.com/NVIDIA/spark-rapids
- github.com/NVIDIA-Merlin
- github.com/NVIDIA/Morpheus
