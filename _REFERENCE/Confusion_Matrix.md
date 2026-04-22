# Confusion Matrix — Full Breakdown

Confusion matrix is the *ground truth* of classification evaluation. Every metric in `Model_Performance_Metrics.md §1-2` is derived from it.

## 1. Binary layout

|                  | **Pred Positive** | **Pred Negative** |
|------------------|-------------------|-------------------|
| **Actual Positive** | TP | FN |
| **Actual Negative** | FP | TN |

- **TP** (True Positive) — predicted + and was +.
- **TN** (True Negative) — predicted - and was -.
- **FP** (False Positive / Type I error) — predicted + but was -.
- **FN** (False Negative / Type II error) — predicted - but was +.

### Memory hook
- **T/F** = prediction right or wrong.
- **P/N** = what model predicted.
- "Type I = False alarm" (FP). "Type II = Miss" (FN).

## 2. Derived metrics (binary)

| Name | Formula | Intuition |
|------|---------|-----------|
| **Accuracy** | (TP+TN)/Total | Overall correctness |
| **Error rate** | (FP+FN)/Total | 1 − Accuracy |
| **Precision (PPV)** | TP/(TP+FP) | Of my positive predictions, how many correct? |
| **Recall / Sensitivity / TPR** | TP/(TP+FN) | Of actual positives, how many did I catch? |
| **Specificity / TNR** | TN/(TN+FP) | Of actual negatives, how many did I correctly reject? |
| **FPR (false-alarm rate)** | FP/(FP+TN) = 1-TNR | x-axis of ROC |
| **FNR (miss rate)** | FN/(FN+TP) = 1-TPR |  |
| **NPV** | TN/(TN+FN) | Of negative predictions, how many correct? |
| **FDR** | FP/(FP+TP) | Of positive predictions, how many wrong? |
| **FOR** | FN/(FN+TN) | Of negative predictions, how many wrong? |
| **Prevalence** | (TP+FN)/Total | Base rate of positives |
| **F1** | 2·PR/(P+R) | Harmonic mean of P and R |
| **F-beta** | (1+β²)·PR / (β²·P+R) | β>1 weights recall, β<1 precision |
| **MCC** | (TP·TN − FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN)) | Balanced for imbalance; [-1, 1] |
| **Balanced Accuracy** | (TPR + TNR)/2 | Correct under imbalance |
| **Cohen's κ** | (p_o − p_e)/(1 − p_e) | Agreement over chance |
| **Youden's J** | TPR + TNR − 1 | Optimal threshold picker |

## 3. Worked example

100 patients screened, 20 actually have disease.
Model predicts 30 positive.
Of those 30, 18 are correct.

| | Pred + | Pred − |
|---|---|---|
| Actual + | TP=18 | FN=2 |
| Actual − | FP=12 | TN=68 |

- Accuracy = (18+68)/100 = 0.86
- Precision = 18/30 = 0.60
- Recall = 18/20 = 0.90
- Specificity = 68/80 = 0.85
- F1 = 2·0.6·0.9/(0.6+0.9) = 0.72
- MCC = (18·68 − 12·2)/√(30·20·80·80) = 1200/√3.84M = 1200/1960 ≈ 0.612

Interpretation:
- Good recall (0.90) — catch most sick patients.
- Moderate precision (0.60) — 40% of alerts are healthy people needing reassurance.
- For cancer screening this is often the right trade (recall > precision).

## 4. Threshold matters

For probabilistic models:
- Default threshold = 0.5.
- Not always optimal.
- **ROC curve** plots TPR vs FPR across thresholds.
- **PR curve** plots Precision vs Recall across thresholds.
- Pick threshold by **business cost matrix**:
  `minimize E[cost] = FP·c_FP + FN·c_FN`.

## 5. Multi-class matrix

N×N. Rows = actual, columns = predicted. Diagonal = correct.

Example 3-class:
```
             Pred A  Pred B  Pred C
Actual A  [   50      2       3  ]
Actual B  [    1     45       4  ]
Actual C  [    3      5      42  ]
```

- Per-class metrics computed vs "one-vs-rest":
  - **Precision_A** = 50 / (50+1+3) = 0.926
  - **Recall_A** = 50 / (50+2+3) = 0.909
- **Macro F1** = mean of per-class F1.
- **Micro F1** = global TP/FP/FN aggregated.
- **Weighted F1** = per-class F1 weighted by support.

## 6. Imbalanced cases

Majority-class baseline often fools accuracy.
- 99% negatives → "predict always negative" = 99% accuracy, zero utility.
- Report **Precision + Recall + F1 + MCC + PR-AUC**, not accuracy.
- Plot per-class confusion matrix.

## 7. Cost-sensitive evaluation

Weight each cell by its real-world cost:
```
Cost = c_TP·TP + c_FP·FP + c_TN·TN + c_FN·FN
```
- c_FP ≈ c_FN only in rare cases (both are usually asymmetric).
- Set cost matrix **before training**, pick threshold + algorithm that minimizes it.

## 8. Calibration on top

Metrics derived from confusion matrix care about *class assignments*, not probabilities.
Add:
- **Brier score** (mean squared prob error).
- **ECE** (Expected Calibration Error).
- **Reliability diagram**.

A model can have 95% accuracy but wildly uncalibrated probs.

## 9. Beyond classification — analogs

- **Object detection**: TP/FP/FN defined by IoU threshold → **AP** curves.
- **Segmentation**: per-pixel TP/FP/FN → IoU / Dice.
- **Retrieval**: TP/FP at each rank k → Precision@k, Recall@k.
- **Anomaly detection**: framed as binary with rare positives; always use PR-AUC.

## 10. How to visualize

- **Matplotlib confusion matrix heatmap** (sklearn `ConfusionMatrixDisplay`).
- **Normalized per row** (% of actual) vs per column (% of predicted) — pick based on question.
- **Stacked bar** — per class breakdown.
- **Sankey** — flow from actual → predicted.
- **Per-segment matrices** — slice by customer cohort / geography / time.

## 11. Python snippets

```python
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_true, y_pred, labels=classes)
print(classification_report(y_true, y_pred, target_names=classes))

ConfusionMatrixDisplay(cm, display_labels=classes).plot(cmap="Blues")
plt.show()
```

Multiclass normalization:
```python
confusion_matrix(y_true, y_pred, normalize="true")   # rows sum to 1 (recall-like)
confusion_matrix(y_true, y_pred, normalize="pred")   # cols sum to 1 (precision-like)
```

## 12. Debugging with confusion matrix

- Off-diagonal hotspot between 2 classes → those two are conflated → add features or data.
- Entire row low recall → class under-represented or ambiguous.
- Entire column low precision → threshold too loose for that class.
- Symmetric confusion (A→B and B→A equally) → labels may overlap / mislabel.

## 13. Common mistakes

1. Comparing F1 across models with different test sets.
2. Averaging per-sample metric when per-class is the right view.
3. Not checking per-segment confusion (e.g., different cameras, cohorts, regions).
4. Using accuracy on imbalanced data.
5. Forgetting that threshold=0.5 is arbitrary.
6. Mixing up rows vs columns when reading a new matrix.

## 14. Summary

- Confusion matrix is the primitive; everything else is a ratio.
- Imbalance makes accuracy dangerous.
- Threshold + cost matrix drive the real metric choice.
- Always inspect per-class + per-segment.
- Pair with probability calibration for a complete picture.

## Refs
- *Pattern Recognition and Machine Learning* — Bishop.
- *The Elements of Statistical Learning* — Hastie, Tibshirani, Friedman.
- *Applied Predictive Modeling* — Kuhn & Johnson.
- `scikit-learn` metrics docs.
