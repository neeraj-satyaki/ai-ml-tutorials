# Computer Vision — Model Families & Architectures

Tree of CV model architectures with key design choice and typical use.

## 1. Convolutional Backbones (pre-ViT era)

### LeNet-5 (LeCun 1998)
Conv(6)-pool-Conv(16)-pool-FC-FC-FC. First successful CNN for digits.

### AlexNet (Krizhevsky 2012)
5 conv + 3 FC, ReLU, dropout, GPU training. Broke ImageNet.

### VGG (Simonyan 2014)
Stacks of 3×3 conv + pool. Very deep (16 or 19 layers). Simple, param-heavy.

### GoogLeNet / Inception (Szegedy 2014)
Inception modules = parallel 1×1, 3×3, 5×5, pool branches. Cheap deep nets.

### ResNet (He 2015)
Residual blocks: x + F(x). Enables 50/101/152/1000-layer training. Foundation for everything after.

### DenseNet (Huang 2016)
Each layer receives all earlier features (concat). Strong feature reuse.

### ResNeXt (Xie 2016)
Grouped convolutions → "cardinality" dimension.

### SENet (Hu 2017)
Squeeze-and-Excitation: per-channel attention. Won ImageNet 2017.

### MobileNet v1/v2/v3 (Howard 2017+)
Depthwise-separable convs → mobile-friendly. v2: inverted residuals; v3: HardSwish + NAS.

### EfficientNet (Tan 2019)
Compound scaling (depth + width + resolution). EfficientNet-B0..B7, then v2.

### RegNet (Radosavovic 2020)
NAS-derived design space; simple linear rules.

### ConvNeXt (Liu 2022)
"Modernized" CNN — ResNet + ViT-style design choices (LN, GELU, large kernels). Matches ViT.

---

## 2. Vision Transformers (ViT era, 2020+)

### ViT (Dosovitskiy 2020)
Image → 16×16 patches → tokens → Transformer encoder → classify. Needs large data.

### DeiT (Touvron 2020)
Data-efficient ViT. Distillation token, augmentation.

### Swin Transformer (Liu 2021)
Windowed attention, shifted windows. Hierarchical. Pyramid feature maps.

### PVT (Wang 2021)
Pyramid Vision Transformer — multi-scale.

### BEiT (Bao 2021) / MAE (He 2021)
Masked Image Modeling: mask 75% patches, reconstruct. Strong self-supervised backbones.

### DINO / DINOv2 (Caron 2021 / Oquab 2023)
Self-distillation. DINOv2 is go-to universal vision backbone (2023+).

### EVA / EVA-02 (BAAI 2022-23)
CLIP-initialized MIM. Strong features.

### SigLIP (Zhai 2023) / CLIP (OpenAI 2021)
Vision-language contrastive pretraining. Open vocabulary everything.

### DiT (Peebles 2022)
Diffusion Transformer (used in Sora, SD3, Flux).

---

## 3. Object Detection

### Two-stage (region proposals → classify)
- **R-CNN** (2013), **Fast R-CNN** (2015), **Faster R-CNN** (2015) — RPN + ROI pooling.
- **Mask R-CNN** (2017) — adds mask branch for instance segmentation.
- **Cascade R-CNN** (2017) — cascaded refinements.

### One-stage (predict boxes directly)
- **YOLO v1 (2015) → v3 → v4 → v5 → v7 → v8 → v9 → v10 (2024)** — real-time det.
- **SSD** (2016) — multi-scale feature maps.
- **RetinaNet** (2017) — focal loss for class imbalance.
- **EfficientDet** (2019) — compound-scaled BiFPN.

### Transformer-based
- **DETR** (2020) — set prediction with transformer decoder. No NMS.
- **Deformable DETR**, **DINO-DETR**, **Co-DETR**, **RT-DETR** (2023) — real-time DETR.

### Open-vocabulary
- **GLIP**, **GroundingDINO** (2023), **YOLO-World** (2024) — detect arbitrary text classes.
- **OWL-ViT / OWL-v2** — Google's open-vocab detector.

---

## 4. Semantic / Instance / Panoptic Segmentation

### Semantic (per-pixel class)
- **FCN** (2014) — first end-to-end fully convolutional segmenter.
- **U-Net** (2015) — encoder-decoder + skip connections (medical imaging standard).
- **SegNet**, **DeepLab v1/v2/v3/v3+** — atrous convolutions, ASPP.
- **PSPNet** — pyramid pooling.
- **SegFormer** (2021) — ViT-based, lightweight.
- **Mask2Former** (2022) — unified mask transformer.

### Instance
- **Mask R-CNN**, **YOLACT**, **SOLO / SOLOv2**, **Mask2Former**.

### Panoptic
- **Panoptic FPN**, **Mask2Former** (unified panoptic).

### Foundation
- **SAM** (Meta 2023), **SAM 2** (Meta 2024, also videos). Prompt-based segmentation.

---

## 5. Pose / Keypoint Estimation

- **OpenPose** (CMU 2017) — multi-person 2D pose.
- **HRNet** (2019) — maintains high-res features throughout.
- **RTMPose** (2023) — real-time 2D/3D.
- **VitPose** (2022) — ViT backbone.
- **SMPL / HMR / PIFuHD** — 3D human mesh.

---

## 6. Depth Estimation

- **MiDaS** (Intel 2019).
- **DPT** — dense prediction transformer.
- **ZoeDepth** (2023) — metric depth.
- **Depth Anything v1/v2** (2024) — universal monocular depth.
- **Marigold** (2023) — diffusion-based depth.

## 7. Optical Flow

- **FlowNet / FlowNet2** (2015-17).
- **PWC-Net** (2018).
- **RAFT** (2020).
- **GMFlow / FlowFormer** (2022).

## 8. OCR

- **CRNN** (CNN+RNN+CTC).
- **PaddleOCR** (practical pipeline).
- **TrOCR** (Transformer OCR).
- **Donut** (2022) — OCR-free document understanding.

## 9. Image Generation

### GANs
- **DCGAN** (2015), **ProGAN** (2017), **StyleGAN v1/v2/v3** (NVIDIA 2018-21), **BigGAN** (2018).

### VAE variants
- **VQ-VAE / VQ-VAE-2** (discrete codebook), **VQGAN** (2020).

### Autoregressive
- **PixelCNN / PixelSNAIL**, **DALL-E v1** (discrete VAE + GPT).

### Diffusion
- **DDPM** (2020) → **Stable Diffusion 1.5/2/XL/3/3.5** → **Flux** (2024) → **Imagen** → **Muse**.
- **ControlNet** (2023) — conditional diffusion.

### Text-to-Video
- **Sora** (OpenAI 2024), **Runway Gen-3**, **Kling**, **Veo 3** (Google), **MovieGen** (Meta), **Hunyuan-Video**, **LTX-Video**.

## 10. 3D / Neural Rendering

- **NeRF** (2020) — neural radiance field.
- **Instant-NGP** (NVIDIA 2022) — hash encoding, seconds to train.
- **3D Gaussian Splatting** (2023) — explicit 3D gaussians, real-time rendering.
- **2D/3D Gaussian Splatting variants** (2024) — DreamGaussian, SuGaR.

## 11. Face / Identity

- **FaceNet** (2015) — triplet loss embeddings.
- **ArcFace** (2019) — additive angular margin.
- **DeepFace**, **InsightFace** libs.

## 12. Medical Imaging

- **U-Net 3D** / **V-Net** — volumetric seg.
- **nnU-Net** — self-configuring; de-facto standard.
- **MONAI** framework.
- **MedSAM** (2024) — SAM fine-tuned for medical.

## 13. Anomaly / Defect Detection

- **PaDiM, PatchCore** (memory-bank features).
- **WinCLIP, APRIL-GAN** — CLIP-based zero-shot industrial anomaly.

## 14. Video Understanding

- **I3D** (2017) — inflated 3D CNN.
- **SlowFast** (2019) — two pathways.
- **TimeSformer** (2021) — space-time attention.
- **VideoMAE / VideoMAE v2** (2022-23).
- **V-JEPA** (2024) — self-supervised video JEPA.

## 15. Visual-Language Multimodal (VLM) 2024-26

- **CLIP** (2021), **SigLIP**, **SigLIP-2** (2024).
- **LLaVA v1/1.5/1.6** (2023-24).
- **GPT-4V / GPT-4o**, **Claude 3/4**, **Gemini 1.5/2.0**.
- **Qwen2-VL**, **Qwen2.5-VL**.
- **InternVL 1/2/2.5**.
- **Molmo** (AllenAI 2024), **Pixtral 12B** (Mistral 2024).
- **Aria** (Rhymes AI 2024), **NVLM** (NVIDIA 2024).

---

## Common design knobs
| Axis | Choices |
|------|---------|
| Backbone | CNN vs Transformer vs Hybrid |
| Resolution | Fixed vs multi-scale vs pyramid |
| Supervision | Supervised vs Self-supervised (MIM, contrastive, DINO) |
| Scale | Task-specific (50-100M) vs foundation (1B-10B+) |
| Output head | classification / detection / seg / dense regression |
