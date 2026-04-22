# Game Development

Engines, rendering, animation, physics, audio, AI, networking, platforms, pipeline, design.

## Engines
**Unity** (URP/HDRP, C#, huge ecosystem), **Unreal 5** (Nanite + Lumen, C++/Blueprints), **Godot 4** (GDScript/C#, OSS, fast iteration), **GameMaker**, **CryEngine**, **O3DE** (Amazon, formerly Lumberyard), **Cocos Creator** (web/mobile 2D), **Bevy** (Rust ECS), **Defold**, **Stride**, **Flax**.

## Core loop
Main loop + fixed timestep. **ECS** (Entity-Component-System) — data-oriented design. Scene streaming. Input systems. State machines + behavior trees. Event messaging. Save/load serialization.

## Rendering
Real-time 3D rasterization + PBR. Global illumination (**Lumen**, VXGI, RTXGI). Shadow maps + RT shadows. Deferred vs forward. Virtualized geometry (**Nanite**). Shader graphs. Texture streaming + virtual textures. HDR + ACES tonemapping. **DLSS / FSR / TSR / XeSS** upscalers. Post-FX (bloom, motion blur, DOF, AA). Niagara / VFX Graph particles. 2D sprites + tilemaps.

## Animation
Skeletal rigging. Skinning (linear-blend / dual quaternion). Blend spaces + state machines. IK (two-bone, FABRIK, full-body). Motion matching. Root motion. Morph / blendshapes. Cutscene timelines. Mocap pipelines. Retargeting (humanoid). Ragdoll physics blending.

## Physics
Rigidbodies, colliders, CCD. Joints/constraints. Cloth, rope, soft-body. Vehicles. Fluids (SPH). Destruction (Chaos, APEX). Character controllers. Navigation meshes. Networked deterministic physics.

## Audio
Spatial audio + HRTF. Convolution reverb. Middleware: **Wwise**, **FMOD**. Ambisonics. Adaptive music. Footsteps, impact. In-game VoIP.

## AI
NavMesh (Recast/Detour). Behavior trees / Utility AI / GOAP. FSM / HFSM. Flocking. Perception (sight/sound/touch). NPC dialogue (Ink, Yarn Spinner). **Procedural generation** (Wave Function Collapse, noise-based biomes). **LLM NPCs** (2023+). Unity ML-Agents for RL.

## Networking
Authoritative client-server. **Rollback netcode (GGPO)** for fighting games. Lockstep deterministic (RTS). Delta compression, snapshot interp, lag compensation. Matchmaking. Dedicated servers (GameLift, PlayFab, K8s). Anti-cheat (EAC, BattlEye, VAC). Cross-play.

## Gameplay patterns
Dialogue + quest + inventory + loot tables. Crafting economy. Damage + buff/debuff systems. Turn vs real-time combat. Day-night + weather. Procedural missions. Dynamic Difficulty Adjustment (DDA). Meta-progression.

## Platforms
PC (Steam, EGS, GOG). Mobile (iOS, Android, Vulkan/Metal). Consoles (PS5, Xbox Series, Switch / Switch 2). **Web (WebGPU)**. Cloud (GeForce NOW, Luna). VR (Quest, Vision Pro, PSVR2).

## Pipeline + tooling
DCC: Blender, Maya, 3ds Max, Houdini. Substance Painter/Designer. ZBrush. **Version control**: Perforce, **Plastic SCM**, Git LFS. Jenkins / TeamCity builds. **RenderDoc**, PIX for graphics debug. Analytics (GameAnalytics, Unity Analytics). A/B tests + LiveOps.

## Design + production
Core loop design. GDD / one-pagers. Playtesting. MDA framework (Mechanics-Dynamics-Aesthetics). Level blockouts → polish. Monetization (IAP, battle pass, season pass). F2P economy design. Accessibility in games. LiveOps.

## Books
- *Game Programming Patterns* — Robert Nystrom (free online).
- *Real-Time Rendering* — Akenine-Möller et al.
- *Game Engine Architecture* — Jason Gregory.
- *Physically Based Rendering* (PBRT) — free online.
- *The Art of Game Design* — Jesse Schell.
- *GDC Vault* (talks, free + paid).
