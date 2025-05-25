# LLM-AI-SRE-Copilot
#  SRE Copilot – Local AI Assistant for SREs

A lightweight, offline-ready AI assistant that helps Site Reliability Engineers (SREs) diagnose incidents, understand logs, and follow runbooks using a **local RAG (Retrieval-Augmented Generation)** system.

Built with:
- [TinyLLaMA](https://ollama.com/library/tinyllama) via Ollama for fast local inference
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [sentence-transformers](https://www.sbert.net/) for fast embeddings

---

## What It Does

1. **Embed Logs + Runbooks:** Vectorize `.txt` files using sentence-transformers.
2. **Store in Vector DB:** Save embeddings in a local ChromaDB.
3. **Ask Questions:** Use a command-line interface to ask questions.
4. **Get Answers:** System retrieves relevant context and queries TinyLLaMA with it.

---

##  Directory Structure

sre-copilot/
├── data/ # Put your .txt runbooks, logs, and incidents here
├── index/ # Vector DB is stored here (auto-generated)
├── embeddings.py # Converts text files into vector embeddings
├── rag.py # Handles context retrieval + TinyLLaMA inference
├── ask.py # CLI assistant interface
├── requirements.txt
└── README.md

---

##  Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
install ollama  
ollama pull tinyllama
python embeddings.py
python ask.py
```

How It Works (RAG Flow)
User asks a question.

Question is embedded and matched against documents in ChromaDB.

Top documents are retrieved and added to the prompt.

Prompt is sent to TinyLLaMA using ollama run.

Response is streamed back to the user.


Why It’s Useful
Fully offline: No OpenAI API or cloud costs.

Fast & tiny (~500MB memory).

Perfect for on-call engineers, postmortem analysis, or local log mining.
