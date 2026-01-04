# AI-Powered CLI Tool for Meeting Transcript Summarization

## 📌 Overview

This project is a command-line interface (CLI) application that automatically generates concise, executive-level summaries from long meeting transcripts using Large Language Models (LLMs).

The tool ingests meeting transcripts in **PDF or text format**, safely processes large documents through **deterministic chunking**, and produces **clear bullet-point summaries** without exceeding model context limits. It is designed to be **fast**, **cost-efficient**, and **reliable** for real-world usage.

---

## 🚀 Features

- 📄 Supports **PDF and TXT** meeting transcripts  
- 🧠 Token-safe, **deterministic chunking** for large documents  
- 🔁 **Multi-stage summarization pipeline** for higher-quality output  
- ⚡ Ultra-low latency inference using **Groq + LLaMA 3.1**  
- 📋 Clean, executive-level **bullet-point summaries**  
- 🖥️ Simple and extensible **CLI interface**

---

## 🛠️ How It Works

The summarization pipeline follows a multi-stage approach:

1. **Text Extraction**  
   Extracts raw text from PDF or text input files.

2. **Chunking**  
   Splits content into safe, character-bounded chunks to avoid exceeding LLM context limits.

3. **Chunk-Level Summarization**  
   Generates focused summaries for each chunk using an LLM.

4. **Final Consolidation**  
   Deduplicates and consolidates all chunk summaries into a final executive summary.

---

## 🧪 Example Usage

```bash
python summarize.py meeting_transcript.pdf
