# FeedbackInsightSystem

# ✈️ Turkish Airlines – Passenger Feedback Insight System (FEIS)

## What is FEIS?

**FEIS (Flight Experience Intelligence System)** is a next-generation, modular AI platform designed for airlines to deeply analyze passenger feedback using state-of-the-art Large Language Model (LLM) orchestration. Built as a multi-agent, node-based architecture, FEIS allows for real-time voice-to-insight workflows, hallucination-resistant outputs, and explainable AI-driven suggestions to drive continuous improvement in aviation.

---

## 🚀 Key Features

- **Voice-to-Insight**: Directly ingest audio (voice feedback) from passengers and instantly convert to actionable text using OpenAI Whisper.
- **Node-Driven Orchestration**: Modular, node-based flow including transcription, RAG (Retrieval-Augmented Generation), hallucination detection, grounding, and CrewAI agent orchestration.
- **Grounded AI**: Built-in hallucination prevention using fact-checking (FFSDB) and smart agent-to-agent (A2A) coordination.
- **Full-stack Demo**: FastAPI backend, Streamlit interactive demo panel, and cloud-ready Docker deployment.
- **CI/CD Ready**: GitHub Actions for build, test, and automatic GCP Cloud Run deployment.

---

## ✨ System Flow

1. **Passenger Feedback (Audio/Voice or Text)**
2. **TranscribeNode**: Audio → Text (OpenAI Whisper)
3. **RAGNode**: Retrieve relevant operational documents (LangChain + Pinecone)
4. **GroundingNode**: Fact-check feedback with FFSDB (fact store)
5. **HallucinationCheckerNode**: Flag hallucinations before agent synthesis
6. **A2AOrchestrationNode**: Coordinate CrewAI agents for consensus
7. **SpeakNode**: (Optional) Respond to user as synthesized voice/text

---

## 🧩 Architecture

- **Multi-Agent (CrewAI):**  
  - Captain, Researcher, Observer, Analyst — each handling a unique perspective in feedback analysis.
- **Modular Node Structure:**  
  - Each task (transcription, retrieval, grounding, orchestration) is a composable Python class (node).
- **Explainability & Trust:**  
  - Hallucination risk flagged and prevented before AI suggestions are shown.
- **Grounding/Fact Store (FFSDB):**  
  - Real-world facts and incident patterns are matched before any AI output.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, FastAPI
- **AI/ML:** OpenAI Whisper, OpenAI LLMs, LangChain, Pinecone, CrewAI
- **Frontend:** Streamlit (optional demo panel)
- **Orchestration:** Node-based pipeline with agent-to-agent (A2A) design
- **CI/CD:** GitHub Actions, Docker, Google Cloud Run

---

## 💡 Why FEIS for Turkish Airlines?

- **Actionable, Explainable Feedback**: Move beyond classic NPS; leverage multi-agent, multi-modal feedback analysis.
- **Production-Ready**: Modular, easily extensible, and instantly cloud-deployable for enterprise use.
- **Future-Proof**: Newest orchestration techniques (LangGraph, CrewAI, Fact Store Grounding, A2A) built-in.

---

## 🚦 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Fill in your .env file with OpenAI & Pinecone API keys

# 3. Start API
uvicorn main:app --reload

# 4. (Optional) Launch demo UI
streamlit run streamlit_app.py

# 5. Try the /analyze_audio endpoint with an audio file
