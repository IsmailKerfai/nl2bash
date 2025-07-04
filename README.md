# NL ➜ Bash

Convert natural language instructions into **safe Bash commands** using local LLMs (powered by Ollama).  
Designed for CLI usage with a focus on simplicity, safety, and local privacy.

---

## Features

-  **Command safety filtering** (blocks `rm`, `shutdown`, etc.)
-  Local LLM (e.g. LLaMA 3 via [Ollama](https://ollama.com/))
-  Few-shot prompting for improved accuracy
-  Unit-tested safety layer
-  Fully modular & CLI-ready

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. Run the translator
```bash
python main.py
```

## Run Tests
```bash
pytest tests/
```
