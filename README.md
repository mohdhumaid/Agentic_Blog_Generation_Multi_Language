# 🧠 Agentic Blog Generation System

An **Agentic AI-powered Blog Generation API** built using **FastAPI, LangGraph, LangChain, and Groq LLMs**.  
The system automatically generates high-quality blog content on a given topic and supports **multi-language translation (e.g., Hindi)** using a graph-based agentic workflow.

---

## 🚀 Features

- 📝 **Automated Blog Generation** from a topic
- 🌐 **Multi-language Translation** (English → Hindi)
- 🧠 **Agentic Workflow** using LangGraph
- ⚡ **FastAPI REST API**
- 🔄 **Stateful Graph Execution**
- 🛡️ **Groq-safe JSON handling (robust parsing)**
- 📦 Clean modular architecture (nodes, graphs, schemas)

---

## 🏗️ Architecture Overview

```

Client (POST /blogs)
│
▼
FastAPI Endpoint
│
▼
LangGraph Agent
├── Blog Generation Node
├── Language Routing Logic
└── Translation Node
│
▼
Final Blog Output (JSON)

```

---

## 📁 Project Structure

```

BlogAgentic/
│
├── app.py                     # FastAPI entry point
├── requirements.txt
│
├── src/
│   ├── graphs/
│   │   └── graph_builder.py   # LangGraph workflow definition
│   │
│   ├── nodes/
│   │   └── blog_node.py       # Blog generation & translation logic
│   │
│   ├── schemas/
│   │   └── blog_schema.py     # Pydantic models (Blog)
│   │
│   └── state/
│       └── blog_state.py      # TypedDict state definition
│
└── README.md

```

---

## 🧪 API Usage

### **Endpoint**
```

POST /blogs

````

### **Request Body**
```json
{
  "topic": "Agentic AI",
  "language": "hindi"
}
````

### **Response**

```json
{
  "blog": {
    "title": "अगेंटिक एआई का उदय",
    "content": "कृत्रिम बुद्धिमत्ता (एआई) के तेजी से विकास..."
  }
}
```

---

## 🧠 Agentic Workflow Logic

1. **Blog Generation Node**

   * Generates an English blog based on the topic
   * Output stored in graph state

2. **Language Router**

   * Checks `current_language`
   * Routes to translation node if required

3. **Translation Node**

   * Translates blog title & content
   * Uses **safe JSON extraction** (Groq-compatible)
   * Updates graph state

---

## 🔐 JSON Safety with Groq

Groq LLMs are strict with function calling and structured output.

This project uses:

* ❌ No `with_structured_output()` for long text
* ✅ Defensive JSON extraction from raw LLM responses
* ✅ Markdown/code-fence tolerant parsing

This ensures **production stability**.

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

```bash
export GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **LangChain**
* **LangGraph**
* **Groq LLM**
* **Pydantic**
* **Uvicorn**

---

## 📌 Key Design Principles

* Stateless API, stateful agent graph
* Clear separation of nodes & orchestration
* Production-safe LLM output handling
* Extensible for more languages & tools

---

## 🔮 Future Enhancements

* 🌍 Add more languages (French, Spanish, Arabic)
* 🧠 Add memory / summarization agent
* 🖼️ Image generation for blogs
* 📄 Markdown / HTML export
* 🧪 Unit tests for nodes & graph

---

## 👨‍💻 Author

**Mohd Humaid**
RPA Developer | Agentic AI Enthusiast
Python • LangGraph • LLMs • Automation

---

## 📜 License

This project is licensed under the MIT License.

```

---

If you want, I can also:
- 🔹 Customize README for **GitHub portfolio**
- 🔹 Add **architecture diagram (Mermaid)**
- 🔹 Write **API documentation section**
- 🔹 Make a **resume-ready project description**

Just tell me 👍
```
