# DBMS — Database Management Systems

Deeper than `SystemDesign/Databases`. Theory → Storage → Query → Transactions → Recovery → Distributed → Types → Admin.

## Theory (`Theory/`)
- Relational model (Codd 1970), relational algebra (σ, π, ⋈, ÷), tuple relational calculus.
- Functional Dependencies, normalization through 6NF.
- ER modeling, set theory foundations.

## Storage (`Storage/`)
- **Pages / heap files** — slotted pages, free-space mgmt.
- **Row-store vs Column-store** — OLTP vs OLAP.
- **Indexes** — B+Tree, LSM-Tree, Hash, Bitmap, Inverted, GIN/GiST/BRIN.
- **TOAST**, **Buffer pool**, **Covering + Partial indexes**.

## Query (`Query/`)
- Parser → Analyzer → Rewriter → Optimizer (cost-based + rule-based) → Executor.
- **Joins** — Nested Loop, Hash, Sort-Merge, Index.
- **Cardinality estimation** via histograms + sampling.
- **Vectorized execution**, compiled/JIT (Umbra, DuckDB), **predicate/projection pushdown**, parallel + adaptive execution, plan caching.

## Transactions (`Transactions/`)
- ACID. Isolation levels (RU, RC, RR, SI, Serializable). Classical anomalies.
- **MVCC** (Postgres, MySQL InnoDB, Oracle).
- **2PL** strict/rigorous, **Timestamp Ordering**, **Serializable Snapshot Isolation** (SSI).
- Deadlock detection/prevention; lock manager; intent locks.
- Optimistic concurrency; distributed sagas.

## Recovery (`Recovery/`)
- **WAL**, **ARIES** (Analysis/Redo/Undo, fuzzy checkpoints).
- Redo/Undo semantics, shadow paging, physical vs logical logging, PITR, backup types.

## Distributed DB (`Distributed/`)
- Partitioning / sharding; replication (leader-follower, multi-leader, leaderless — Dynamo).
- Consistency models (Lin, Seq, Causal, Eventual).
- CAP + PACELC. Paxos/Raft consensus. 2PC/3PC.
- Clocks (Lamport, vector, HLC, TrueTime).
- Anti-entropy, read-repair, hinted handoff, gossip.

## Types (`Types/`)
OLTP, OLAP, HTAP, NewSQL, NoSQL (KV, document, column-family, graph), TimeSeries, VectorDB, Search, Embedded (SQLite), Multi-model, Object DB.

## Admin / Ops (`Admin_Ops/`)
Query tuning (EXPLAIN ANALYZE), index tuning, vacuum/analyze, partitioning, read replicas, pooling (PgBouncer), online DDL migrations, HA, monitoring (pg_stat_*), upgrades.

## Core systems to learn deeply
Postgres (gold standard OSS), MySQL/InnoDB, SQLite, Cassandra, DynamoDB, Redis, Elasticsearch/OpenSearch, ClickHouse, DuckDB, BigQuery, Snowflake, CockroachDB/Spanner, Kafka (log), Neo4j.

## Books
- *Database System Concepts* — Silberschatz, Korth, Sudarshan.
- *Database Internals* — Alex Petrov.
- *Readings in Database Systems* (Red Book) — Stonebraker, Hellerstein.
- *Designing Data-Intensive Applications* — Kleppmann.
- *Transaction Processing* — Gray, Reuter (classic).
