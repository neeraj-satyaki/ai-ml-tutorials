# Deep Learning for Audio — Speech, Music, Sound

All audio inference + processing tasks with ML/DL — classical DSP foundations through frontier audio LLMs.

## Fundamentals (`Fundamentals/`)
Waveform basics, sampling rate + Nyquist, PCM quantization. STFT + spectrogram, mel spectrogram, MFCC, chroma features, pitch (F0), harmonicity. Libraries: **librosa**, **torchaudio**.

## Classic DSP (`ClassicDSP/`)
Windowing (Hann, Hamming). OLA/WOLA. Filter banks. Classical denoising (Wiener, spectral subtraction). Acoustic Echo Cancellation (AEC). Beamforming (MVDR, GSC). VAD (energy, WebRTC-VAD). Phase vocoder. Time-stretching / pitch-shifting. Dereverb (WPE).

## Speech Recognition (ASR) (`SpeechRecognition_ASR/`)
- **Classical**: HMM-GMM.
- **Neural**: CTC, LAS, RNN-T, Transformer, **Conformer**, **wav2vec 2.0**, **HuBERT**, **Whisper** (OpenAI 2022; v3 2023), **Canary / Parakeet** (NVIDIA 2024).
- **Streaming ASR**: chunked Conformer, cache-aware streaming.
- Low-resource via self-supervised pretraining.
- Speech translation (ST). Keyword spotting + wake-words. Forced alignment (MFA). Language ID. Code-switching.

## Text-to-Speech (TTS) (`TextToSpeech_TTS/`)
- **Acoustic models**: Tacotron 1/2, FastSpeech 1/2.
- **Vocoders**: WaveNet → WaveRNN → MelGAN → HiFi-GAN → UnivNet → BigVGAN.
- **End-to-end**: **VITS**, **NaturalSpeech 2/3**, **StyleTTS 2** (2023).
- **Zero-shot / cloning**: **XTTS v2** (Coqui), **Bark** (Suno), **F5-TTS** (2024), **MegaTTS**, **OpenVoice**.
- **Neural codecs**: **EnCodec** (Meta), **SoundStream** (Google), **Mimi** (Kyutai). Basis of audio LMs.
- Emotional TTS, voice conversion, voice biometrics + safety.

## Speaker Recognition / Diarization (`SpeakerRecognition_Diarization/`)
Speaker embeddings: x-vector, **ECAPA-TDNN**. Diarization: **pyannote.audio**, **NVIDIA NEMO**. Verification. Anti-spoofing (ASVspoof challenge). Voice print biometric risks.

## Music AI (`MusicAI/`)
- Genre/tagging, beat/tempo/downbeat, key detection.
- **Source separation**: Spleeter, **Demucs**, MDX, **BSRNN**.
- **Music transcription** (AMT).
- **Music generation**: **MusicLM** (Google), **MusicGen** (Meta), **Stable Audio** (Stability), **AudioCraft**, **Suno v3.5/v4**, **Udio**, **AudioBox** (Meta).
- Symbolic music (MIDI). Lyrics alignment. Cover-song ID, query-by-humming, similarity retrieval, drum transcription, chord recognition.

## Sound Event Detection / Tagging (`SoundEventDetection_Tagging/`)
- Audio tagging: **YAMNet**, **PANNs** on AudioSet.
- SED (localize in time). Acoustic scene classification (DCASE challenges).
- Bio-acoustics (BirdCLEF). Industrial anomaly audio. Fire/gunshot. UrbanSound8K.

## Speech Enhancement / Denoise (`SpeechEnhancement_Denoise/`)
- **RNNoise**, **Demucs-audio**, **Voicefixer**, **DeepFilterNet**.
- Dereverb DNN. Speech separation: **Conv-TasNet**, **SepFormer**, **Mossformer2** (2024).
- Deep AEC, PLC (packet loss concealment), bandwidth extension.

## Self-Supervised Audio Embeddings (`AudioEmbeddingsSelfSup/`)
**wav2vec / wav2vec 2.0**, **HuBERT**, **WavLM**, **data2vec**, **BEATs**, **AudioMAE**, **CLAP** (contrastive lang-audio), **AudioCLIP**, **LAION-CLAP**.

## Audio-VLM / Multimodal (`AudioVLM_Multimodal/`)
- **AudioGPT**, **LTU** (Listen-Think-Understand), **SALMONN**, **Qwen-Audio / Qwen2-Audio**.
- **GPT-4o realtime**, **Gemini Live**, **Claude voice** (via Anthropic speech mode).
- **Voicebox** (Meta), **Hallo / Spark-Audio**, end-to-end audio LLMs.
- **Lip-sync**: Wav2Lip, **MuseTalk**, **SadTalker**, **EMO** (Alibaba 2024).

## Streaming / Realtime (`StreamingRealtime/`)
Low-latency ASR (chunked). Streaming TTS. Real-time VAD. Voice assistant pipeline: wake-word → VAD → ASR → LLM → TTS → playback. Barge-in / interrupt handling. End-pointing. Jitter buffers. **WebRTC audio stack**, **Opus codec**, **EVS**, neural codecs live.

## Audio Safety / Forensics (`AudioSafety_Forensics/`)
Deepfake voice detection. **AudioSeal** (Meta 2024) — audio watermarking. Voice-print anti-spoof. Bias/fairness across accents/dialects. Privacy + voice anonymization.

---

## End-to-End Stacks (common)

### Voice Assistant
`mic → WebRTC VAD → Whisper (streaming) → LLM → XTTS v2 → audio out`

### Call-center Analytics
`PSTN → Diarization → ASR → sentiment + topic LLM → dashboards`

### Music Production AI
`MIDI / text → MusicGen or Suno → stems via Demucs → mastering`

### Podcast Pipeline
`raw audio → enhance (DeepFilterNet) → diarize → ASR → summaries + chapters → TTS re-narration`

### Accessibility Captioning
`live stream → streaming Whisper → captions overlay on video`

## Books / refs
- *Speech and Language Processing* — Jurafsky & Martin.
- *Audio Source Separation and Speech Enhancement* — Vincent et al.
- Interspeech, ICASSP, ISMIR proceedings.
- Meta AudioCraft repo, OpenAI Whisper repo, NVIDIA NeMo, pyannote.audio.
