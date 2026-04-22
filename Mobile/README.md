# Mobile Development

iOS, Android, cross-platform. Bridges `Frontend/`, `DL/ComputerVision/` (on-device).

## iOS (`iOS/`)
- **Swift** + **SwiftUI** (declarative); UIKit (imperative).
- **Combine** + **async/await** concurrency.
- **Metal** (GPU), **Core ML**, **VisionKit**, **ARKit + RealityKit**.
- WidgetKit + Live Activities, App Clips, StoreKit 2, CloudKit, BackgroundTasks, PushKit, SharePlay, **App Intents / Siri Shortcuts**.

## Android (`Android/`)
- **Kotlin** (+ Coroutines + Flow).
- **Jetpack Compose** (modern UI) vs View system (XML legacy).
- Architecture: MVVM / MVI. Navigation, Hilt / Koin DI, Room / SQLDelight, DataStore, WorkManager.
- **CameraX**, **MediaPipe**, **TFLite / LiteRT**, **ML Kit**.
- NDK + JNI for native code.
- Gradle KTS, ProGuard / R8 shrinking.
- Play Console, App Bundle.

## Cross-platform (`CrossPlatform/`)
- **Flutter** (Dart) — Skia / Impeller renderer.
- **React Native** (+ Expo / EAS) — Fabric renderer, Hermes JS.
- **Kotlin Multiplatform** + **Compose Multiplatform**.
- Ionic/Capacitor, Xamarin → .NET MAUI, NativeScript.

## On-device AI (`OnDeviceAI/`)
- Core ML optimization, TFLite, **MediaPipe Tasks**, ONNX Runtime Mobile.
- **Qualcomm QNN** (Snapdragon NPU), **Apple MLX**.
- LLMs on-device: **llama.cpp** (mobile), **MLC-LLM**, Gemini Nano, Apple Foundation Models (iOS 18+).
- MobileSAM / MobileSAM 2 for segmentation on phone.
- Edge TPU Coral.

## Performance / UX (`PerformanceUX/`)
Battery profiling. Cold vs warm startup time. ANR avoidance (Android). 60/120 fps rendering. Memory leaks (Instruments, LeakCanary). Jank detection. Offline-first data. Local-first sync (CRDTs: Yjs, Automerge).

## Security (`Security/`)
Keychain / Keystore. Biometrics. Attestation (DeviceCheck, Play Integrity, App Attest). Certificate pinning. Code obfuscation (R8, Hermes, Bitcode). ATS/TLS hardening. MDM / MAM integration. Mobile SBOM.

## Release + Store (`Release_Store/`)
CI/CD: Fastlane, Bitrise, **EAS (Expo)**, Xcode Cloud, GitHub Actions with macOS runners. TestFlight / Play Internal Testing. Crashlytics, Sentry. A/B testing (Firebase, Amplitude). Remote config + feature flags. In-App Review.

## Books + refs
- *iOS App Development with Swift* — Apple Developer docs (free).
- *Android Developers* (developer.android.com).
- *Flutter in Action* — Eric Windmill.
- Hacking with Swift (Paul Hudson).
- Google Codelabs + Apple Tutorials.
