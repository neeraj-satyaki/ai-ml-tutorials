# One-Iteration Math Derivations per Architecture

For each architecture: tiny example, forward pass math, loss, backward pass math, one weight update.

Notation: x = input, W = weight, b = bias, L = loss, η = lr, σ = sigmoid.

---

## 1. MLP (2-layer, binary classification)

**Architecture**
- Input: x ∈ ℝ² = [1, 2]
- W¹ ∈ ℝ^{2×2}, b¹ ∈ ℝ²; W² ∈ ℝ^{1×2}, b² ∈ ℝ.
- Activation: ReLU hidden, sigmoid output. Loss: Binary CE.

**Init (pick simple values)**
- W¹ = [[0.1, 0.2],[0.3, 0.4]], b¹ = [0, 0]
- W² = [0.5, 0.6], b² = 0
- y_true = 1, η = 0.1

**Forward**
- z¹ = W¹x + b¹ = [0.1·1+0.2·2, 0.3·1+0.4·2] = [0.5, 1.1]
- a¹ = ReLU(z¹) = [0.5, 1.1]
- z² = W²·a¹ + b² = 0.5·0.5 + 0.6·1.1 = 0.25 + 0.66 = 0.91
- ŷ = σ(0.91) = 1/(1+e^{-0.91}) ≈ 0.7130
- L = −[y log ŷ + (1−y) log(1−ŷ)] = −log(0.7130) ≈ 0.3384

**Backward (chain rule)**
- ∂L/∂z² = ŷ − y = 0.7130 − 1 = −0.2870     (sigmoid + BCE simplification)
- ∂L/∂W² = ∂L/∂z² · a¹ᵀ = −0.2870 · [0.5, 1.1] = [−0.1435, −0.3157]
- ∂L/∂b² = −0.2870
- ∂L/∂a¹ = (W²)ᵀ · ∂L/∂z² = [0.5, 0.6]·−0.2870 = [−0.1435, −0.1722]
- ∂L/∂z¹ = ∂L/∂a¹ ⊙ ReLU'(z¹) = [−0.1435·1, −0.1722·1] = [−0.1435, −0.1722]
- ∂L/∂W¹ = ∂L/∂z¹ · xᵀ = [[−0.1435·1, −0.1435·2],[−0.1722·1, −0.1722·2]] = [[−0.1435, −0.2870],[−0.1722, −0.3444]]
- ∂L/∂b¹ = [−0.1435, −0.1722]

**Update (SGD)**
- W² ← W² − η·∂L/∂W² = [0.5, 0.6] − 0.1·[−0.1435, −0.3157] = [0.5144, 0.6316]
- W¹ ← W¹ − η·∂L/∂W¹
  - Row 1: [0.1, 0.2] − 0.1·[−0.1435, −0.2870] = [0.1144, 0.2287]
  - Row 2: [0.3, 0.4] − 0.1·[−0.1722, −0.3444] = [0.3172, 0.4344]

---

## 2. CNN (1 conv layer, no pooling, 1 output class)

**Architecture**
- Input X ∈ ℝ^{3×3} (grayscale image).
- Kernel K ∈ ℝ^{2×2}, stride 1, valid → feature map F ∈ ℝ^{2×2}.
- Flatten → single Linear → sigmoid → BCE.

**Init**
- X = [[1,2,0],[3,1,0],[0,0,1]], K = [[1,0],[0,-1]], W_fc=[0.1,0.2,0.3,0.4], b_fc=0, y=1, η=0.1.

**Forward — convolution**
- F[0,0] = 1·1 + 2·0 + 3·0 + 1·(−1) = 0
- F[0,1] = 2·1 + 0·0 + 1·0 + 0·(−1) = 2
- F[1,0] = 3·1 + 1·0 + 0·0 + 0·(−1) = 3
- F[1,1] = 1·1 + 0·0 + 0·0 + 1·(−1) = 0
- F = [[0, 2],[3, 0]]; flatten = [0, 2, 3, 0].
- z = W_fc·flat = 0.1·0 + 0.2·2 + 0.3·3 + 0.4·0 = 1.3
- ŷ = σ(1.3) ≈ 0.7858; L = −log(0.7858) ≈ 0.2411.

**Backward**
- δ_z = ŷ − y = −0.2142
- ∂L/∂W_fc = δ_z · flat = [0, −0.4284, −0.6427, 0]
- ∂L/∂flat = δ_z · W_fc = [−0.0214, −0.0428, −0.0643, −0.0857]
- Reshape to ∂L/∂F = [[−0.0214, −0.0428],[−0.0643, −0.0857]].
- Conv gradient wrt kernel (cross-correlation of input with ∂L/∂F):
  - ∂L/∂K[0,0] = Σ X[i,j]·∂L/∂F[i,j] where window at (0,0) → 1·−0.0214 + 2·−0.0428 + 3·−0.0643 + 1·−0.0857 = −0.3910
  - Similarly compute K[0,1], K[1,0], K[1,1]. Standard formula:
    **∂L/∂K = X ⋆ ∂L/∂F** (cross-correlation).

**Update**
- K ← K − η · ∂L/∂K.

---

## 3. RNN (vanilla, 1 hidden unit, sequence length 2)

**Architecture**
- h_t = tanh(W_x x_t + W_h h_{t-1} + b)
- ŷ = σ(W_y h_T)

**Init**
- x₁=1, x₂=0.5; h₀=0; W_x=0.5, W_h=0.8, b=0, W_y=1; y=1, η=0.1.

**Forward**
- z₁ = 0.5·1 + 0.8·0 = 0.5; h₁ = tanh(0.5) ≈ 0.4621
- z₂ = 0.5·0.5 + 0.8·0.4621 = 0.25 + 0.3697 = 0.6197; h₂ = tanh(0.6197) ≈ 0.5505
- ŷ = σ(1·0.5505) ≈ 0.6343; L = −log(0.6343) ≈ 0.4551

**Backward (BPTT)**
- δ_out = ŷ − y = −0.3657
- ∂L/∂W_y = δ_out · h₂ = −0.2013
- ∂L/∂h₂ = δ_out · W_y = −0.3657
- ∂L/∂z₂ = ∂L/∂h₂ · (1 − h₂²) = −0.3657·(1 − 0.3031) = −0.2549
- ∂L/∂W_x (from t=2) = ∂L/∂z₂ · x₂ = −0.1275
- ∂L/∂W_h (from t=2) = ∂L/∂z₂ · h₁ = −0.1178
- ∂L/∂h₁ = ∂L/∂z₂ · W_h = −0.2039
- ∂L/∂z₁ = ∂L/∂h₁ · (1 − h₁²) = −0.2039·(1 − 0.2135) = −0.1603
- ∂L/∂W_x (from t=1) = ∂L/∂z₁ · x₁ = −0.1603
- Total ∂L/∂W_x = −0.1275 + −0.1603 = −0.2878
- Total ∂L/∂W_h = −0.1178 + (∂L/∂z₁·h₀=0) = −0.1178

**Update**
- W_x ← 0.5 − 0.1·(−0.2878) = 0.5288
- W_h ← 0.8 − 0.1·(−0.1178) = 0.8118
- W_y ← 1 − 0.1·(−0.2013) = 1.0201

Note: BPTT sums gradients across time through shared weights.

---

## 4. LSTM (one time step, 1 hidden unit)

**Cell equations**
- f_t = σ(W_f·[h_{t-1}, x_t] + b_f)    (forget gate)
- i_t = σ(W_i·[h_{t-1}, x_t] + b_i)    (input gate)
- c̃_t = tanh(W_c·[h_{t-1}, x_t] + b_c)  (candidate)
- c_t = f_t⊙c_{t-1} + i_t⊙c̃_t
- o_t = σ(W_o·[h_{t-1}, x_t] + b_o)    (output gate)
- h_t = o_t⊙tanh(c_t)

**Tiny forward** (all weights 0.5, biases 0, x=1, h₀=0, c₀=0):
- z = W·[0, 1] + 0 = 0.5 (same for all 4 gates with these weights)
- f = σ(0.5) = 0.6225; i = 0.6225; c̃ = tanh(0.5) = 0.4621; o = 0.6225
- c = 0.6225·0 + 0.6225·0.4621 = 0.2877
- h = 0.6225 · tanh(0.2877) = 0.6225 · 0.2801 = 0.1744

**Backward sketch**
- Each gate gets δ from ∂L/∂h and ∂L/∂c.
- ∂L/∂o = ∂L/∂h · tanh(c); ∂L/∂c = ∂L/∂h · o · (1−tanh²(c)) + ∂L/∂c_next·f_next.
- Then for each gate g ∈ {f,i,c̃,o}: ∂L/∂z_g = ∂L/∂g · g'(z_g) with appropriate derivative (sigmoid or tanh). Backprop to W_g via z_g·[h_{t-1}, x_t]ᵀ.
- BPTT unrolls this across T time steps. Gates' sigmoids prevent vanishing (gradient through c can flow when f_t≈1).

---

## 5. Transformer (single attention head, seq len 2, d=2)

**Architecture (one block of single-head attention)**
- Q = X W_Q, K = X W_K, V = X W_V
- A = softmax(QKᵀ/√d)
- Z = A V

**Tiny values**
- X = [[1, 0],[0, 1]], W_Q=W_K=W_V=I (identity, 2×2). d=2.
- Q = X = [[1,0],[0,1]]; K = X; V = X.
- QKᵀ = [[1·1+0·0, 1·0+0·1],[0·1+1·0, 0·0+1·1]] = [[1,0],[0,1]].
- Scaled: /√2 = [[0.707, 0],[0, 0.707]].
- Softmax rowwise:
  - row 0: softmax([0.707, 0]) = [e^{0.707}, 1]/(e^{0.707}+1) = [2.028/3.028, 1/3.028] = [0.670, 0.330].
  - row 1: [0.330, 0.670].
- Z = A·V = [[0.670·1 + 0.330·0, 0.670·0 + 0.330·1],[0.330·1+0.670·0, 0.330·0+0.670·1]] = [[0.670, 0.330],[0.330, 0.670]].

**Backward sketch (one step)**
- Suppose L = ||Z − Y||² / 2, with target Y (given).
- ∂L/∂Z = Z − Y.
- ∂L/∂V = Aᵀ · ∂L/∂Z.
- ∂L/∂A = ∂L/∂Z · Vᵀ.
- Softmax back: if s = softmax(u), ∂L/∂u_i = s_i (∂L/∂s_i − Σ_j s_j ∂L/∂s_j).
- Apply row-wise: ∂L/∂(QKᵀ/√d) → divide by √d → flows to Q and K via ∂L/∂Q = (∂L/∂S)·K, ∂L/∂K = (∂L/∂S)ᵀ·Q (where S=QKᵀ/√d).
- Finally ∂L/∂W_Q = Xᵀ·∂L/∂Q, etc. Update weights by SGD.

---

## 6. VAE (encoder → reparam → decoder)

**Architecture**
- Encoder gives μ, logσ² from x.
- z = μ + σ ⊙ ε, ε ~ N(0,I).   (reparameterization trick enables grads through z)
- Decoder reconstructs x̂ = f(z).
- L = BCE(x, x̂) + KL(N(μ,σ²) || N(0,I))
  - KL (closed form) = −½ Σ(1 + logσ² − μ² − σ²)

**Tiny example** (x scalar, latent dim=1):
- Encoder (simplified): μ = 0.5, logσ² = 0.0 → σ=1.
- ε sampled, say ε = 0.1 → z = 0.5 + 1·0.1 = 0.6.
- Decoder: x̂ = σ(2z) = σ(1.2) ≈ 0.7685. Target x=1.
- Recon loss = BCE(1, 0.7685) ≈ 0.2633.
- KL = −½(1 + 0 − 0.25 − 1) = −½(−0.25) = 0.125.
- Total L ≈ 0.3883.

**Backward (sketch)**
- ∂L/∂x̂ = −(x/x̂ − (1−x)/(1−x̂))
- Prop to z via decoder weights; propagate through z = μ + σε:
  - ∂z/∂μ = 1, ∂z/∂σ = ε, ∂σ/∂logσ² = σ/2.
- ∂L_KL/∂μ = μ. ∂L_KL/∂logσ² = ½(σ² − 1).
- Sum recon + KL gradients for μ, logσ². Then backprop through encoder.

---

## 7. GAN (one G, D update)

**Loss**
- D: max E[log D(x)] + E[log(1 − D(G(z)))]
- G: min E[log(1 − D(G(z)))]  or −E[log D(G(z))] (non-saturating)

**Tiny values**
- Real x=0.8. Noise z=0.3. G(z) simplified linear: G(z)=2z=0.6. D simplified: D(a)=σ(a)=1/(1+e^{-a}).
- D(x)=σ(0.8)=0.6900; D(G(z))=σ(0.6)=0.6457.
- L_D = −[log(0.6900) + log(1 − 0.6457)] = −[−0.3711 − 1.0383] = 1.4094.
- L_G (non-sat) = −log(0.6457) = 0.4374.

**Updates (sketch)**
- ∂L_D/∂D(x) = −1/D(x); ∂L_D/∂D(G(z)) = 1/(1−D(G(z))). Backprop through D params.
- ∂L_G/∂G(z) = (−1/D(G(z))) · D'(G(z)) · 1. Backprop through G params (D frozen).
- Alternate: D step, then G step.

---

## 8. GCN (one graph conv step)

**Formula:** H^(l+1) = σ(Ã H^(l) W^(l)), where Ã = D^{−1/2}(A+I)D^{−1/2}.

**Tiny graph**: 3 nodes, edges {(0,1),(1,2)}.
- A = [[0,1,0],[1,0,1],[0,1,0]]. A+I = identity + A. Degrees = [2, 3, 2] (with self-loop).
- Ã computed entrywise (see example.py).
- H^(0) = [[1,0],[0,1],[1,1]] (node features, d=2). W^(0) = [[1,0],[0,1]] = I (for brevity).
- Ã H W has shape (3, 2); apply ReLU.

**Backward:** ∂L/∂W = H^(l)ᵀ Ãᵀ (∂L/∂H^(l+1) ⊙ σ'). ∂L/∂H^(l) = Ãᵀ (∂L/∂H^(l+1) ⊙ σ') W^(l)ᵀ. Backprop through each layer.

---

## 9. DDPM (one training step)

**Forward noising**: x_t = √(ᾱ_t) x₀ + √(1 − ᾱ_t) ε, ε ~ N(0,I).
**Loss**: simple objective — L = E_{x₀, t, ε} || ε − ε_θ(x_t, t) ||².

**Example** (1-D toy):
- x₀ = 0.8, t random (say t=50), ε sampled = 0.3, ᾱ_{50} = 0.6.
- x_t = √0.6 · 0.8 + √0.4 · 0.3 = 0.620 + 0.190 = 0.810.
- Assume ε_θ(x_t, t) = 0.1 (untrained prediction).
- L = (0.3 − 0.1)² = 0.04.
- ∂L/∂ε_θ = 2(ε_θ − ε) = 2(0.1 − 0.3) = −0.4.
- Backprop this through the U-Net / DiT weights.

**Reverse step (at inference)**: x_{t-1} = (1/√α_t) (x_t − (β_t/√(1−ᾱ_t)) ε_θ(x_t, t)) + σ_t z, with z ~ N(0,I).
