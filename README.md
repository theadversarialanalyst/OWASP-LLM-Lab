# OWASP Top 10 for LLM Applications (2026 Edition) — Hands-On Exploit Lab

[![Security: Defensive & Offensive](https://img.shields.io/badge/Security-Offensive%20%26%20Defensive-red.svg)](#)
[![Environment: Local Sandbox](https://img.shields.io/badge/Environment-Local%20Docker%20%2F%20Python-blue.svg)](#)
[![Channel: The Adversarial Analyst](https://img.shields.io/badge/YouTube-The%20Adversarial%20Analyst-black.svg)](https://www.youtube.com/@theadversarialanalyst)

Welcome to the definitive hands-on repository for the **OWASP Top 10 for LLM Applications (2026 Edition)**, curated by **The Adversarial Analyst**.

Most enterprise AI teams are deployment-obsessed and security-blind. They are shipping wrappers, RAG pipelines, and autonomous agents at breakneck speed, blindly trusting that foundational model providers solved security at the core. Spoiler: They didn't. 

This repository accompanies the video series. We do not do corporate compliance theater or dry slide decks. We build vulnerable architectures locally, write the exploits, execute them, and then write the production-grade secure code required to remediate them.

---

## 📑 Series & Repository Roadmap

Each directory in this repository corresponds to a specific video in the series, containing a target vulnerable application, an offensive exploit script (`exploit.py`), and a secured remediation patch (`secure.py` or equivalent config).

```
📂 OWASP-LLM-Lab
│
├── 📂 01_master_class_overview        # Diagnostic tooling & architecture threat models
├── 📂 02_llm01_prompt_injection       # Direct override & Indirect RAG injections
├── 📂 03_llm02_sensitive_disclosure   # System memory extraction & context sniffing
├── 📂 04_llm03_supply_chain           # Poisoned Hugging Face weights & dependency hijacking
├── 📂 05_llm04_model_poisoning        # Fine-tuning backdoors & vector payload injection
├── 📂 06_llm05_insecure_output        # LLM-to-XSS and SSRF execution via unsanitized rendering
├── 📂 07_llm06_excessive_agency       # Autonomous agent hijacking (RCE via tool abuse)
├── 📂 08_llm07_prompt_leakage          # System prompt exfiltration techniques
├── 📂 09_llm08_vector_weaknesses       # Cross-tenant data bleeding in vector databases
├── 📂 10_llm09_misinformation         # Hallucination exploits & blind execution vulnerabilities
└── 📂 11_llm10_unbounded_consumption  # Recursive agent looping & Token DoS vectors
```

## 🏗️ The Local Attack Surface Target

Before you start breaking the applications, you must understand the generic architecture you are spinning up container-by-container throughout this course:

```
[User Input / Attacker]
           │
           ▼
┌───────────────────────┐
│ React / Next.js UI    │ ──(Insecure Output Handling -> Stored XSS)
└───────────────────────┘
│
▼
┌───────────────────────┐      ┌───────────────────────────┐
│ FastAPI Backend App   │ ────>│ Vector Database (Chroma)  │
└───────────────────────┘      └───────────────────────────┘
│                     (RAG & Embedding Poisoning)
▼
┌───────────────────────┐      ┌───────────────────────────┐
│ LLM Orchestration     │ ────>│ Autonomous Agents & Tools │
│ (LangChain/LlamaIndex)│      └───────────────────────────┘
└───────────────────────┘         (Excessive Agency -> RCE)
│
▼
[Local Ollama / OpenAI API]

```

## ⚙️ Prerequisites & Global Setup

To keep your host machine clean and isolate the target vulnerabilities, everything runs locally via Docker and Python virtual environments. 

### 1. System Requirements
*   **Python 3.10+**
*   **Docker & Docker Compose**
*   **Ollama** (Optional, for running models entirely locally without burning API quotas)

### 2. Initialization
Clone the repository and run the diagnostic check to ensure your local environment is configured properly for the labs:

```bash
# Clone the lab repository
git clone [https://github.com/theadversarialanalyst/OWASP-LLM-Lab.git](https://github.com/theadversarialanalyst/OWASP-LLM-Lab.git)
cd OWASP-LLM-Lab

# Run the environment diagnostic script
python3 01_master_class_overview/environment_check.py
```

If the diagnostic script flags errors (e.g., missing Docker daemon or outdated Python versions), resolve them before proceeding to 02_llm01_prompt_injection.

🛡️ Disclaimer
CRITICAL NOTE: The code provided in this repository is explicitly designed to be structurally vulnerable for educational and research purposes. Do not deploy code from the vulnerable directories into production environments. The exploits demonstrated are intended exclusively for local validation, red-teaming education, and authorized security assessments.

🤝 Community & Contribution
If you discover a sleeker bypass, a tighter exploit script, or a more optimal secure coding remediation for any of the labs, open a Pull Request. Keep the fluff out of the description; let the code do the talking.

YouTube Channel: [The Adversarial Analyst](https://www.youtube.com/@theadversarialanalyst)

Keep Learning: Don't just patch the symptom; re-architect the pipeline.