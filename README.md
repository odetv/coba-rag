# Coba RAG

Coba RAG adalah project yang dirancang untuk membantu memahami dan mengimplementasikan Retrieval Augmented Generation (RAG), sebuah pendekatan yang menggabungkan pencarian informasi (retriever) dan generasi teks (generator) untuk membangun aplikasi AI yang cerdas dan responsif. Project ini cocok untuk pengembang, peneliti, dan siapa saja yang ingin mempelajari cara mengintegrasikan RAG ke dalam aplikasi berbasis model bahasa besar (LLM).

## Teknologi

- [Python](https://www.python.org/): Bahasa pemrograman untuk membuat Virtual Assistant.
- [Langchain](https://www.langchain.com/): Framework untuk mengelola alur kerja RAG.
- [Ollama](https://ollama.com/): Embedding RAG gratis.
- [Groq](https://groq.com/): Model RAG gratis.
- [FAISS](https://faiss.ai/): Penyimpanan vector database.

## Modul Pengenalan RAG

[Download MODUL RAG.pdf](modul/MODUL%20RAG.pdf)

## Instalasi Project

Clone project

```bash
  git clone https://github.com/odetv/coba-rag.git
```

Masuk ke direktori project

```bash
  cd coba-rag
```

Persiapkan environment python

```bash
  pip install virtualenv
  python -m venv venv
  venv/Scripts/activate (jika OS Windows)
  source venv/bin/activate (jika macOS/Linux)
```

Install packages requirements

```bash
  pip install -r requirements.txt
```

Buat dan lengkapi file environment variabel (.env)

```bash
  OLLAMA_BASE_URL="YOUR_OLLAMA_BASE_URL"
  GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

Build vector database

```bash
  python process.py
```

Sesuaikan pertanyaan di `main.py`

```bash
  rag("Sesuaikan Pertanyaan Disini")
```

Jalankan dengan CLI

```bash
  python main.py
```

## Authors

- [@odetv](https://www.github.com/odetv)
- [@DiarCode11](https://github.com/DiarCode11)
