# Natural Language Processing

From classical tokenization through modern LLM frontier. Bridges to `DL/Transformer/`, `AI/Frontier2024_2026/`, `AI/Agentic/`.

## Fundamentals (`Fundamentals/`)
Tokenization (BPE, WordPiece, SentencePiece, tiktoken), normalization (stemming, lemmatization), stop words, POS tagging, morphology, n-grams, regex, Unicode normalization (NFC/NFKC).

## Classical (`Classical/`)
- **Bag-of-words**: TF-IDF, BM25.
- **Latent models**: LSI/LSA, LDA topic modeling.
- **Sequence labeling**: HMM, CRF.
- **Embeddings**: Word2Vec (skip-gram / CBOW), GloVe, FastText, Doc2Vec.
- **Parsing**: dependency + constituency parsing.

## Tasks (`Tasks/`)
- Text classification, sentiment, NER, relation extraction.
- Intent + slot filling (conversational).
- Coreference, SRL, entity linking, event extraction.
- Summarization (extractive + abstractive), MT, QA, reading comprehension.
- Dialog systems (task-oriented + chit-chat).
- Text generation, paraphrase, style transfer, grammar correction.
- STS, NLI, discourse + coherence.

## LLM Era (`LLM_Era/`)
Pretraining corpora, tokenizer training. CausalLM vs MaskedLM vs Seq2Seq. Scaling laws (Kaplan → Chinchilla → inference-time). Instruction tuning (SFT). Preference tuning (DPO, GRPO, IPO, ORPO, SimPO). Tool use + function calling. Structured outputs (JSON mode). Grounding + RAG patterns. Long context + NIH evals. Prompt caching. Guardrails (Llama Guard, NeMo Guardrails).

## Evaluation (`Evaluation/`)
- **Generation**: BLEU, ROUGE, METEOR, ChrF, BERTScore, COMET, BLEURT.
- **QA**: EM, F1 (SQuAD-style).
- **LM**: Perplexity.
- **Preference**: Arena Elo, MT-Bench, AlpacaEval, pairwise human eval, LLM-as-judge.
- **Capability benchmarks**: MMLU, GPQA, HellaSwag, ARC, TruthfulQA, BBH, IFEval, AGIEval.
- **Serving**: latency, TTFT, tokens/s, throughput.
- **Safety + bias**: WMDP, Biased-Q, CrowS-Pairs, BBQ.

## Frameworks (`Frameworks/`)
- HF Transformers, Datasets, Tokenizers, PEFT, Accelerate.
- Sentence-Transformers.
- spaCy, NLTK, Stanza, Gensim, Flair.
- RAG + agent: Haystack, LangChain, LlamaIndex, DSPy, Guidance, Outlines, Instructor.
- Serving: vLLM, SGLang, TGI, TensorRT-LLM, LMDeploy.

## Multilingual (`Multilingual/`)
Language ID (fastText, CLD3). Transliteration. Cross-lingual embeddings (LASER, LaBSE). Multilingual models (XLM-R, mT5, NLLB). Low-resource NLP. Code-switching. Script handling.

## Code Models (`Code_Models/`)
Code-Llama, StarCoder, CodeGen, Qwen 2.5-Coder, DeepSeek-Coder. Fill-in-the-middle (FIM). Benchmarks: HumanEval, MBPP, LiveCodeBench, SWE-Bench, RepoBench. Agentic coding (Cursor, Claude Code, Aider, Devin, OpenDevin, SWE-agent).

## Safety + Ethics (`Safety_Ethics/`)
Toxicity detectors, PII redaction, jailbreak detection, prompt-injection defenses, hallucination detection, copyright attribution, LLM watermarking (Kirchenbauer, SynthID).

## Books + refs
- *Speech and Language Processing* — Jurafsky & Martin (free draft).
- *Natural Language Processing with Transformers* — Tunstall et al.
- HF course: huggingface.co/learn/nlp-course.
- ACL / EMNLP / NAACL proceedings.
