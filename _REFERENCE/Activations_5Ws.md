# Activation Functions — 5Ws

Every common activation with: **What** (formula), **Why** (purpose), **Where** (typical use), **When** (timeline / adoption), **Who** (introducer / paper).

Activations introduce nonlinearity — without them an N-layer net collapses to a single linear transform.

---

## 1. Sigmoid (Logistic)
- **What:** σ(x) = 1 / (1 + e^(-x)) ∈ (0, 1). Derivative: σ(1-σ).
- **Why:** Squashes to probability-like [0,1]. Smooth, differentiable.
- **Where:** Output of binary classifier; gate activations in LSTM/GRU.
- **When:** 1958+. Dominant hidden activation pre-2010; mostly replaced by ReLU in hidden layers.
- **Who:** Logistic function (Verhulst 1845); popularized in perceptrons (Rosenblatt), backprop (Rumelhart, Hinton, Williams 1986).
- **Watch out:** Saturates (~0 gradient at |x| large) → vanishing gradients. Not zero-centered.

## 2. Tanh
- **What:** tanh(x) = (e^x − e^(-x)) / (e^x + e^(-x)) ∈ (−1, 1). Derivative: 1 − tanh².
- **Why:** Zero-centered → faster convergence than sigmoid.
- **Where:** RNNs, LSTMs/GRUs (cell nonlinearity), older MLPs.
- **When:** Long-known. Default for RNNs in the 90s-2010s.
- **Who:** Classical math function; used by LeCun et al. 1998 ("Efficient BackProp").
- **Watch out:** Still saturates; vanishing gradient.

## 3. ReLU
- **What:** ReLU(x) = max(0, x). Derivative: 1 if x>0 else 0.
- **Why:** Non-saturating for x>0 → fixes vanishing gradient; sparse activations; cheap.
- **Where:** Default hidden activation in modern CNNs, MLPs.
- **When:** Proposed 2010, mainstream after AlexNet (2012).
- **Who:** Glorot, Bordes, Bengio (2011) — "Deep Sparse Rectifier Neural Networks". Used in AlexNet (Krizhevsky et al. 2012).
- **Watch out:** "Dying ReLU" — neuron stuck at 0 forever when input always negative.

## 4. Leaky ReLU
- **What:** LeakyReLU(x) = max(αx, x), usually α=0.01.
- **Why:** Small negative slope stops dying-ReLU.
- **Where:** Discriminator of GANs (DCGAN), some CNNs.
- **When:** 2013.
- **Who:** Maas, Hannun, Ng (2013) — "Rectifier Nonlinearities Improve NN Acoustic Models".

## 5. PReLU (Parametric ReLU)
- **What:** Like Leaky but α is learned per channel.
- **Why:** Let network pick negative slope.
- **Where:** Image classifiers (e.g., MSRA ResNet variants).
- **When:** 2015.
- **Who:** He et al. (2015) — "Delving Deep into Rectifiers" (also introduced He initialization).

## 6. RReLU (Randomized ReLU)
- **What:** α sampled uniformly from (l, u) during training, fixed to mean at eval.
- **Why:** Regularization.
- **Where:** Kaggle NDSB winning entries; limited mainstream use.
- **When:** 2015.
- **Who:** Xu, Wang, Chen, Li (2015).

## 7. ELU (Exponential Linear Unit)
- **What:** ELU(x) = x if x>0 else α(e^x − 1).
- **Why:** Negative values push mean activations toward zero → faster learning; smooth at 0.
- **Where:** Some CNNs.
- **When:** 2015.
- **Who:** Clevert, Unterthiner, Hochreiter (2015).

## 8. SELU (Scaled ELU)
- **What:** λ · ELU(x) with specific λ≈1.0507, α≈1.6733.
- **Why:** Self-normalizing — preserves mean 0, var 1 through deep nets (no BatchNorm needed).
- **Where:** SNNs (Self-Normalizing Neural Networks).
- **When:** 2017.
- **Who:** Klambauer, Unterthiner, Mayr, Hochreiter (2017).

## 9. GELU (Gaussian Error Linear Unit)
- **What:** GELU(x) = x · Φ(x), where Φ is Gaussian CDF. Approx: 0.5 x (1 + tanh(√(2/π)(x + 0.044715 x³))).
- **Why:** Smooth probabilistic ReLU; x weighted by "how likely positive".
- **Where:** Transformers — BERT, GPT-2, GPT-3, GPT-4, Vision Transformers.
- **When:** 2016 (paper), ubiquitous since 2018 with BERT.
- **Who:** Hendrycks, Gimpel (2016) — "Gaussian Error Linear Units".

## 10. Swish / SiLU (Sigmoid Linear Unit)
- **What:** Swish(x) = x · σ(βx). With β=1 = SiLU. Smooth, non-monotonic.
- **Why:** Empirically better than ReLU on deep nets.
- **Where:** EfficientNet, MobileNetV3, SSD for detection, many modern CNNs/Transformers.
- **When:** SiLU 2016 (Elfwing et al.); Swish 2017 (rediscovered, named).
- **Who:** Elfwing, Uchibe, Doya (2016); Ramachandran, Zoph, Le (2017) — Google Brain "Searching for Activation Functions".

## 11. Mish
- **What:** Mish(x) = x · tanh(softplus(x)) = x · tanh(ln(1 + e^x)).
- **Why:** Smooth, bounded-below, unbounded-above; small empirical improvements over Swish.
- **Where:** YOLOv4, some CV backbones.
- **When:** 2019.
- **Who:** Misra (2019).

## 12. Softmax
- **What:** softmax(x_i) = e^(x_i) / Σ_j e^(x_j). Outputs sum to 1.
- **Why:** Multi-class probability distribution over logits.
- **Where:** Final layer of multi-class classifiers; attention weights in Transformers.
- **When:** Long-standing.
- **Who:** Boltzmann distribution (1870s physics); Bridle (1990) popularized for NNs.
- **Watch out:** Numerical overflow — use log-sum-exp trick.

## 13. Softplus
- **What:** softplus(x) = ln(1 + e^x). Smooth ReLU. Derivative = sigmoid.
- **Why:** Smooth, always positive output.
- **Where:** Variance head of VAE, reparam to positive scales.
- **When:** 2001.
- **Who:** Dugas, Bengio, Bélisle, Nadeau, Garcia (2001).

## 14. Softsign
- **What:** softsign(x) = x / (1 + |x|). Smooth bounded.
- **Why:** Alternative to tanh with polynomial tails → less saturation.
- **Where:** Rare in practice.
- **Who:** Turian, Bergstra, Bengio (2009).

## 15. Hard Sigmoid / Hard Tanh
- **What:** Piecewise linear approximations. HardSigmoid(x) = clip(0.2x + 0.5, 0, 1).
- **Why:** Fast on CPU / mobile / embedded.
- **Where:** MobileNet-style quantized nets.

## 16. HardSwish
- **What:** x · ReLU6(x+3) / 6.
- **Why:** Swish without expensive sigmoid; fast on mobile.
- **Where:** MobileNetV3.
- **When:** 2019.
- **Who:** Howard et al. (2019) — "Searching for MobileNetV3".

## 17. GLU (Gated Linear Unit)
- **What:** GLU(x) = (xW + b) ⊙ σ(xV + c). Splits → one branch acts as gate.
- **Why:** Learnable multiplicative gating; controls info flow.
- **Where:** Gated CNNs for language (Dauphin), gated decoders.
- **When:** 2016.
- **Who:** Dauphin, Fan, Auli, Grangier (2016).

## 18. SwiGLU
- **What:** SwiGLU(x) = Swish(xW₁) ⊙ (xW₂). GLU variant with Swish gate.
- **Why:** Top-performing FFN activation in large Transformers.
- **Where:** LLaMA, PaLM, GLM, many 2023+ LLMs.
- **When:** 2020.
- **Who:** Shazeer (2020) — "GLU Variants Improve Transformer".
- **Note:** Uses 3 weight matrices (W₁, W₂, W₃) instead of 2; often dim scaled to keep params matched.

## 19. GeGLU / ReGLU
- **What:** GLU variants using GELU or ReLU as gate.
- **Why:** Same family as SwiGLU; slightly different tradeoffs.
- **Where:** Some T5 variants, Flan-T5.
- **Who:** Shazeer (2020).

## 20. Maxout
- **What:** maxout(x) = max(W₁x + b₁, W₂x + b₂, ...). Learns piecewise linear.
- **Why:** Can approximate any convex function; strong with dropout.
- **Where:** Rare now; theoretical interest.
- **When:** 2013.
- **Who:** Goodfellow, Warde-Farley, Mirza, Courville, Bengio (2013).

## 21. Softmin
- **What:** softmax applied to −x; inverse-weighted distribution.
- **Where:** Rare; attention variants.

## 22. Bent Identity
- **What:** (√(x²+1) − 1)/2 + x. Smooth, mildly nonlinear.
- **Where:** Niche; academic curiosity.

---

## Choice cheat sheet

| Context | Pick |
|---------|------|
| Modern Transformer FFN | **SwiGLU / GeGLU** |
| Transformer activation (in attn/FFN) | **GELU** |
| Generic CNN / MLP hidden | **ReLU** (default) |
| Modern CNN (EfficientNet, MobileNetV3) | **Swish / HardSwish** |
| RNN hidden | **tanh** |
| LSTM/GRU gates | **sigmoid** (gates) + **tanh** (candidate/cell) |
| Binary classifier output | **sigmoid** |
| Multi-class output | **softmax** |
| GAN discriminator hidden | **LeakyReLU** |
| Mobile / quantized | **HardSwish / HardSigmoid** |
| Self-normalizing (no BN) | **SELU** |

## Trends timeline
- **Pre-2010:** sigmoid, tanh dominate.
- **2011-2012:** ReLU revolution (AlexNet).
- **2013-2015:** LeakyReLU, PReLU, ELU.
- **2016-2017:** GELU, Swish/SiLU.
- **2018+:** GELU standard in Transformers (BERT, GPT).
- **2020+:** SwiGLU in LLMs (PaLM, LLaMA, Mistral, modern GPTs).

## Key properties to evaluate
1. Saturation (vanishing grad?)
2. Zero-centered?
3. Smoothness (differentiable everywhere?)
4. Computational cost.
5. Monotonic?
6. Bounded?
