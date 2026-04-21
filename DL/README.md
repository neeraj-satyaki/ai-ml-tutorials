# Deep Learning — Architectures & Computer Vision Tasks

## Architectures

### Feedforward (`FeedForward/MLP/`)
Universal approximator. Stack of Linear + nonlinearity.

### Convolutional (`CNN/`)
- **LeNet** — original digit classifier.
- **ResNet** — skip connections enable 100+ layer training.

### Recurrent (`RNN/`)
- **VanillaRNN** — h_t = tanh(Wx + Uh).
- **LSTM** — gated, cell state, long memory.
- **GRU** — simpler than LSTM, fewer params.

### Transformer (`Transformer/`)
Attention-only, parallelizable.
- **BERT** — bidirectional encoder, masked LM pretraining.
- **GPT** — causal decoder, next-token prediction.

### Autoencoder (`Autoencoder/`)
- **VanillaAE** — compress → reconstruct.
- **VAE** — probabilistic latent; KL + recon loss; generative.

### GAN (`GAN/DCGAN/`)
Generator vs Discriminator adversarial game. Sharp samples but mode collapse.

### Graph NN (`GraphNN/GCN/`)
H' = σ(Ã H W). Node features aggregated from neighbors.

### Diffusion (`Diffusion/DDPM/`)
Forward: add noise. Reverse: learn denoising. SOTA for image/video.

---

## Computer Vision Tasks (`ComputerVision/`)
Types of visual inference.

| Task | What output | Typical model |
|------|-------------|---------------|
| **ImageClassification** | label for whole image | ResNet, EfficientNet, ViT |
| **ObjectDetection** | bounding boxes + labels | Faster R-CNN, YOLO v1-v10, DETR, RT-DETR |
| **SemanticSegmentation** | pixel-level class mask | U-Net, DeepLab, SegFormer |
| **InstanceSegmentation** | per-object mask + label | Mask R-CNN, SOLO |
| **PanopticSegmentation** | semantic + instance unified | Panoptic FPN, Mask2Former |
| **KeypointDetection_Pose** | human/object keypoints | OpenPose, HRNet, RTMPose |
| **OCR** | text from image | CRNN, TrOCR, PaddleOCR |
| **DepthEstimation** | per-pixel depth | MiDaS, DPT, ZoeDepth, Depth Anything |
| **OpticalFlow** | per-pixel motion vectors | FlowNet, RAFT, GMFlow |
| **ImageCaptioning** | natural-language description | CNN+RNN → BLIP, GIT |
| **VideoActionRecognition** | action label for clip | I3D, SlowFast, TimeSformer, VideoMAE |
| **3DReconstruction_NeRF_GaussianSplatting** | 3D scene from 2D views | NeRF, Instant-NGP, 3D Gaussian Splatting |
| **ImageGeneration** | synthesize images | DCGAN → StyleGAN → SDXL → Flux → Sora (video) |
| **FaceRecognition** | identity match / embed | FaceNet, ArcFace |
| **MedicalImaging** | lesion / organ / disease | U-Net 3D, nnU-Net, MONAI |
| **VisionAnomalyDetection** | defect / outlier mask | PatchCore, PaDiM, WinCLIP |
| **VisionTransformers_ViT** | backbone for all above | ViT, Swin, DeiT, DINOv2 |
| **SAM_SegmentAnything** | prompt-conditioned mask | Meta's SAM / SAM 2 |
| **OpenVocabulary_Detection** | detect arbitrary text classes | GroundingDINO, OWL-ViT, YOLO-World |

---

### Modern CV pipeline
1. Backbone (ViT or ConvNeXt) pretrained self-supervised (DINOv2 / MAE).
2. Task head (det / seg / pose).
3. Foundation shortcuts: CLIP for zero-shot; SAM for masks; Depth Anything for depth.
