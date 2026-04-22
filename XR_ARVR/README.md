# XR / AR / VR / Spatial Computing

Immersive compute. Bridges `DL/ComputerVision/`, `Mobile/`, `Robotics/`.

## Fundamentals (`Fundamentals/`)
- **6DoF vs 3DoF** tracking.
- SLAM: **inside-out** (Quest, Vision Pro) vs outside-in (Vive lighthouse).
- World tracking, anchors, plane detection, mesh reconstruction.
- **Hand tracking**, eye tracking + foveated rendering.
- Spatial audio (HRTF, binaural).
- Haptics.

## Platforms (`Platforms/`)
- **Meta Quest 3 / 3S / Pro** + Horizon OS.
- **Apple Vision Pro** (visionOS).
- **Pico** (ByteDance).
- **HoloLens 2** (Microsoft MR).
- **Magic Leap 2**.
- **HTC Vive**.
- **WebXR** (browser).

## Engines (`Engines/`)
- **Unity** + XR Interaction Toolkit.
- **Unreal** + OpenXR.
- **Godot** XR.
- **WebXR**: Three.js, Babylon.js.
- **RealityKit** + Reality Composer Pro (visionOS).
- **StereoKit** (C# cross-platform MR).
- **OpenXR** spec — standard API.

## Graphics / Rendering (`Graphics_Rendering/`)
Stereo rendering (single-pass instanced). Foveated rendering (eye-tracked + fixed). MSAA vs FXAA vs TAA. Shaders (HLSL / GLSL). PBR. **NeRF / 3D Gaussian Splatting** in XR. Passthrough AR. Pose prediction + TimeWarp / Asynchronous Space Warp.

## Input + UX (`InputUX/`)
Vision Pro gaze + pinch. Hand gestures. 6-DoF controllers. Voice input. 3D GUI design. Comfort ratings. Motion sickness mitigation (locomotion modes, FOV vignette, frame rate). Accessibility in XR.

## AI in XR (`AI_in_XR/`)
Persistent / cloud anchors. Semantic scene understanding. Scene reconstruction with 3D Gaussian Splatting. Avatar systems (Codec Avatars, VRM). Photogrammetry. Relighting from XR capture. **LLM voice copilot inside XR** (Vision Pro + Gemini Live / Claude voice).

## Industry apps (`Industry_Apps/`)
Training + simulation. Design review (CAD in XR). Medical + surgical planning. Retail virtual try-on. Remote collaboration (Workrooms, Horizon Workrooms). Location-based entertainment (Sandbox VR).

## Toolchain
- Unity XR Interaction Toolkit, XR Hands, AR Foundation.
- Meta XR SDK / Movement SDK / Depth API.
- visionOS SDK + Reality Composer Pro.
- OpenXR + Khronos validation.

## Books + refs
- *3D User Interfaces* — LaViola et al.
- *Unity XR Cookbook*.
- Meta developer docs, Apple visionOS docs.
- IEEE VR / ACM CHI / SIGGRAPH proceedings.
