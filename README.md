# LangGraph AI Content Pipeline

A simple AI workflow built using **LangGraph** and **LangChain** that processes text through multiple AI agents.

## 🚀 Features

This project demonstrates a sequential multi-agent workflow where each agent performs a specific task:

### 📝 Editor Agent
- Fixes grammar and spelling mistakes
- Improves sentence structure
- Refines the overall tone

### 🎬 Script Writer Agent
- Converts the edited text into a natural, engaging YouTube-style script

### 🌐 Translator Agent
- Localizes the script into natural Hinglish for an Indian audience

The workflow is orchestrated using **LangGraph**, with each agent represented as a node in the graph.

---

## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- OpenAI-Compatible API
- FreeLLMAPI
- python-dotenv

---

## 🤖 LLM Provider

This project uses **FreeLLMAPI**, an OpenAI-compatible API proxy, to interact with language models.

Configuration is done using environment variables.

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
MODEL_NAME=auto
```

The application connects using:

```python
base_url = "http://localhost:3001/v1"
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

---

## 📁 Project Structure

```
.
├── project.py
├── requirements.txt
├── .env               # Not committed
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

Create and activate a virtual environment.

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python project.py
```

---

## 🔄 Workflow

```
START
   │
   ▼
📝 Editor Agent
   │
   ▼
🎬 Script Writer Agent
   │
   ▼
🌐 Translator Agent
   │
   ▼
END
```

---

## 📌 Example Pipeline

**Input**

```
Hello, I am a software engineer. I love to code and solve problems.
```

↓

**Editor Agent**
- Corrects grammar
- Improves readability

↓

**Script Writer Agent**
- Converts it into an engaging YouTube script

↓

**Translator Agent**
- Produces a natural Hinglish version

---

## 🚀 Future Improvements

- Add conditional routing
- Add memory support
- Multi-language translation
- Streamlit/Web UI
- Human-in-the-loop review
- Support multiple LLM providers
- Logging & monitoring
- Parallel agent execution

---

## 📚 What I Learned

This project helped me understand:

- LangGraph state management
- Building multi-agent AI workflows
- Node and edge creation
- StateGraph compilation
- Prompt engineering
- Integrating OpenAI-compatible APIs using FreeLLMAPI
- Using LangChain with custom LLM endpoints

---

## 📄 License

This project is created for learning and educational purposes.