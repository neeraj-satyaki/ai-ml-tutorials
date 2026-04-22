# Model Performance Metrics — ML, DL, CV, LLM

One doc, all metrics. Pick metric **before** training. Picking after = p-hacking.

See also: `_REFERENCE/Confusion_Matrix.md` for the matrix-derived metrics deep dive.

---

## 1. Classification (binary)

| Metric | Formula | Use when |
|--------|---------|----------|
| **Accuracy** | (TP+TN)/N | classes balanced |
| **Precision** | TP/(TP+FP) | FP cost high (spam, fraud charge) |
| **Recall (Sensitivity, TPR)** | TP/(TP+FN) | FN cost high (cancer, churn) |
| **Specificity (TNR)** | TN/(TN+FP) | false alarm cost |
| **F1** | 2PR/(P+R) | balance P/R |
| **F-beta** | (1+β²)PR/(β²P+R) | weight recall (β>1) or precision (β<1) |
| **Matthews Corr Coef (MCC)** | balanced for imbalanced data; [-1,1] |
| **Balanced accuracy** | (TPR+TNR)/2 | imbalance |
| **Cohen's κ** | agreement vs chance | inter-rater / imbalance |
| **AUC-ROC** | area under ROC | threshold-free ranking |
| **AUC-PR (Avg Precision)** | area under PR | imbalanced (rare positive) |
| **Log loss / Cross entropy** | prob-calibrated loss |
| **Brier score** | mean squared prob error | calibration |
| **Expected Calibration Error (ECE)** | reliability diagram gap | calibration |

### ROC vs PR — when which
- **Balanced** → ROC fine.
- **Imbalanced (e.g., 1% positive)** → ROC misleadingly optimistic; use **PR curve** + **AP**.

---

## 2. Classification (multiclass)

- **Macro avg** — per-class metric then unweighted mean → equal weight, sensitive to rare classes.
- **Micro avg** — global TP/FP/FN → dominated by frequent classes, = accuracy for multiclass.
- **Weighted avg** — by support.
- **Per-class confusion matrix** — always look at it.
- **Top-k accuracy** — prediction in top-k logits.
- **Softmax cross-entropy**.

---

## 3. Multi-label classification

- **Hamming loss** = fraction of wrong labels per sample.
- **Subset accuracy (exact match)** — all labels correct.
- **Macro/Micro F1** — as above per label.
- **Label ranking avg precision**.

---

## 4. Regression

| Metric | Formula | Notes |
|--------|---------|-------|
| **MSE** | Σ(y-ŷ)²/n | penalizes outliers |
| **RMSE** | √MSE | same units as y |
| **MAE** | Σ\|y-ŷ\|/n | outlier-robust |
| **Huber** | MSE/MAE hybrid | robust regression |
| **MAPE** | mean \|(y-ŷ)/y\| | scale-free; breaks on y=0 |
| **sMAPE** | symmetric MAPE | bounded |
| **MASE** | MAE/naive-MAE | time series forecasting |
| **R²** | 1 - SSres/SStot | can be negative |
| **Adjusted R²** | penalizes features |
| **RMSLE** | RMSE on log(y+1) | skewed targets |
| **Pearson r / Spearman ρ** | correlation |
| **Quantile loss** | pinball loss | quantile regression |

---

## 5. Ranking / Information Retrieval

- **Precision@k**, **Recall@k**.
- **MRR** (Mean Reciprocal Rank).
- **NDCG@k** (graded relevance).
- **MAP** (Mean Average Precision — diff def than detection).
- **Hit rate @k**.

---

## 6. Clustering / unsupervised

- **Silhouette** — [-1, 1], higher better.
- **Davies-Bouldin** — lower better.
- **Calinski-Harabasz** — higher better.
- **Adjusted Rand Index (ARI)** — vs labels.
- **Normalized Mutual Info (NMI)** — vs labels.
- **Fowlkes-Mallows**.
- **Homogeneity + Completeness + V-measure**.

---

## 7. Time series

- **MAPE / sMAPE / MASE**.
- **Forecast bias** (mean residual).
- **Coverage of prediction intervals** (PICP).
- **Direction accuracy**.
- **CRPS** (Continuous Ranked Probability Score) — probabilistic forecasts.

---

## 8. Object Detection (CV)

- **IoU** (Intersection over Union) between box_pred and box_gt.
- **AP** per class: area under per-class PR curve with IoU threshold.
  - **AP@0.5** (PASCAL VOC).
  - **AP@0.5:0.95** step 0.05 (COCO default, a.k.a. **mAP**).
- **mAP** = mean AP over classes.
- **AR** (Avg Recall) at N detections.
- **AP_small / AP_medium / AP_large**.

---

## 9. Semantic / Instance Segmentation

- **IoU / mIoU** (mean over classes).
- **Pixel accuracy** (often misleading — dominated by background).
- **Dice coefficient** = 2·\|A∩B\| / (\|A\|+\|B\|) = F1 for masks.
- **Boundary F1 (BF)**.
- **PQ** (Panoptic Quality) = SQ × RQ. Jointly eval semantic + instance.

## 10. Tracking / MOT

- **MOTA** — accuracy (FP+FN+IDSW).
- **MOTP** — localization precision.
- **IDF1** — identity F1.
- **HOTA** — modern default (joint detection + assoc + localization).
- **IDSW** — ID switches count.
- Cross-camera: IDF1-global, IDP, IDR.

## 11. Pose / Keypoints

- **OKS** (Object Keypoint Similarity) — analog of IoU.
- **AP-OKS @ thresholds** (COCO keypoints).
- **PCK** (Percentage of Correct Keypoints) at threshold fraction of bbox.

## 12. Depth / Disparity

- **AbsRel**, **SqRel**, **RMSE**, **δ<1.25** (thresholded accuracy).
- **Scale-invariant log error (SILog)**.

## 13. Generative (images)

- **FID** (Fréchet Inception Distance) — lower better.
- **Inception Score (IS)** — higher better (legacy).
- **CLIP score** — prompt-image similarity.
- **LPIPS** — perceptual distance.
- **KID** — unbiased FID alternative.
- **PSNR / SSIM / MS-SSIM** — reference-based recon quality.
- **DINO / DreamSim** — identity / similarity preserve.
- Human eval — still gold.

## 14. ASR / Speech

- **WER** (Word Error Rate) = (S+D+I)/N.
- **CER** (Char Error Rate).
- **MER, WIL, WIP**.
- **RTF** (Real-Time Factor) — latency normalized.
- **PESQ, STOI** — perceptual speech quality (for TTS / enhancement).
- **UTMOS, NISQA** — neural MOS.

## 15. Translation / Generation

- **BLEU** — n-gram precision; used for MT baselines.
- **chrF / chrF++** — character n-gram.
- **METEOR** — synonym-aware.
- **BERTScore** — embedding similarity.
- **COMET / BLEURT** — learned metrics; current default for MT.
- **ROUGE (1/2/L)** — summarization, recall-oriented.
- **Exact Match / F1** (SQuAD QA).

## 16. LLM-specific

- **Perplexity** (lower better).
- **Task benchmarks**: MMLU, GPQA, HumanEval, SWE-bench, MATH, AIME, HellaSwag, ARC, TruthfulQA, IFEval, BBH, AGIEval, LongBench, NIH, RULER.
- **Preference**: Arena Elo, MT-Bench, AlpacaEval, pairwise human eval.
- **Faithfulness** (RAG): Ragas metrics, TruLens triad (groundedness, relevance, context relevance).
- **Hallucination rate** on golden set.
- **Toxicity / bias** evals.
- **Operational**: TTFT, tok/s, p50/p95/p99, $/task, cache hit rate.
- See `_REFERENCE/LLM_Evals.md`.

## 17. Recommendation

- **Precision@k**, **Recall@k**, **NDCG@k**, **MAP**.
- **AUC on implicit feedback**.
- **Hit rate**, **coverage**, **diversity**, **serendipity**.
- **Online**: CTR, conversion, revenue/session, A/B.

## 18. Calibration

- **ECE** (Expected Calibration Error).
- **Reliability diagrams**.
- **Brier score**.
- Post-hoc: **temperature scaling**, **isotonic regression**, **Platt scaling**.

## 19. Fairness / bias

- **Demographic parity** — equal positive rates across groups.
- **Equal opportunity** — equal TPR across groups.
- **Equalized odds** — equal TPR + FPR.
- **Disparate impact ratio**.
- Pick one — these three are mathematically incompatible (Chouldechova 2017).

## 20. Efficiency / operational

- **Latency** p50/p95/p99.
- **Throughput** QPS / tok/s.
- **Model size** params, MB.
- **FLOPs / MACs**.
- **Peak GPU memory**.
- **Energy / CO₂** (`codecarbon`, MLCO2).
- **$/inference**.

---

## Picking the right metric

1. What decision does the model support?
2. What error costs more — FP or FN, or both symmetric?
3. Is class distribution balanced?
4. Will the metric be used at training time (differentiable)? Or only eval?
5. Does it match user-visible outcome?

**Principle**: metric you optimize → metric the model will exploit. Pick carefully.

---

## Anti-patterns

- Picking accuracy on imbalanced data.
- ROC-AUC on very rare positive class (use PR-AUC).
- BLEU for dialogue (poor human correlation).
- R² with non-linear target.
- Single point estimate without confidence interval — bootstrap the metric.
- Evaluating on train set "just to check".
- Different preprocessing at eval vs prod.

## Tools

- **scikit-learn** `metrics` module (classification, regression, clustering).
- **torchmetrics** (DL-first).
- **COCO API** (detection + seg).
- **pycocotools**, **motmetrics**, **jiwer** (WER), **sacrebleu**, **bert-score**, **ragas**.
- **evaluate** (HF) — wraps many.
- **cleanlab** — finds label errors affecting metrics.

## Books / refs
- *Pattern Recognition and Machine Learning* — Bishop (probabilistic metrics).
- *Evaluating Learning Algorithms* — Japkowicz & Shah.
- COCO / HOTA paper / CLIPScore papers.
- `scikit-learn` docs on metric selection.
