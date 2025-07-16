# 🧠 AI-TRIP_PLANNER

_Transforming Travel Dreams Into Seamless Adventures_

![Last Commit](https://img.shields.io/github/last-commit/Aniru18/Ai-Trip_Planner?label=last%20commit)
![Python](https://img.shields.io/badge/python-100%25-blue)
![Languages](https://img.shields.io/github/languages/count/Aniru18/Ai-Trip_Planner)

---

## ⚙️ Built with the tools and technologies:

![Markdown](https://img.shields.io/badge/-Markdown-black?logo=markdown&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![TOML](https://img.shields.io/badge/-TOML-brown)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi)
![LangChain](https://img.shields.io/badge/-LangChain-darkgreen)
![Python](https://img.shields.io/badge/-Python-3670A0?logo=python&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=white)
![HTML](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white)
![Pydantic](https://img.shields.io/badge/-Pydantic-ea2678?logo=pydantic&logoColor=white)
![YAML](https://img.shields.io/badge/-YAML-red?logo=yaml&logoColor=white)

---

## ✨ Project Overview

AI-Trip_Planner is a powerful intelligent travel assistant that helps users create personalized travel plans using natural language. Built with LangChain, React, and FastAPI, it delivers a seamless multi-agent experience with real-time integrations.

---

## 🚀 Key Features

- 🧭 **AI-Powered Planning** — Natural language trip generation using LLMs
- 🧩 **Modular Tools** — Easily extend tools for weather, currency, hotels, etc.
- 🌐 **API Integration** — Weather, currency, Google Places, and more
- 📄 **PDF & Markdown Export** — Save plans as `.pdf` or `.md` files
- 🌍 **Frontend App** — React-based UI with HTML/CSS support
- ⚡ **Multi-agent Workflow** — Supports task delegation and automation
- 🪄 **Streamlit Interface** — Optional lightweight demo UI
- 🧑‍💻 **FastAPI Backend** — Secure and performant backend
- 📜 **Error Handling** — Graceful handling of failures and fallbacks

---

## 🧩 Tech Stack

| Layer       | Technology |
|-------------|------------|
| 🧠 LLMs      | Gemini, Groq |
| 🛠️ Backend  | FastAPI, LangChain |
| 🌍 Frontend | React, HTML, CSS |
| 📊 APIs     | Google Places, Tavily, Weather, Currency |
| 📄 Export   | ReportLab, Markdown |
| 🔁 Runtime  | `uv`, `venv`, `Python 3.10+` |



## ⚙️ Installation & Setup

### ✅ Step 1: Install [uv](https://github.com/astral-sh/uv)

```bash
pip install uv
```

---

### ✅ Step 2: Initialize the Project

```bash
uv init Ai_Trip_Planner
```

---

### ✅ Step 3: Create & Activate Virtual Environment

```bash
uv venv env --python cpython-3.10.18-windows-x86_64-none
```

```bash
# Activate on Windows
.\env\Scripts\activate
```

```bash
# Activate on macOS/Linux
source env/bin/activate
```

💡 If using **conda**, run:

```bash
conda deactivate
```

---

### ✅ Step 4: Install All Requirements

```bash
uv pip install -r requirements.txt
```

**Or manually install:**

```bash
uv add langchain langchain-community langchain-experimental fastapi python-dotenv streamlit uvicorn
```

---

### ✅ Step 5: Run the Backend (FastAPI)

```bash
uvicorn main:app --reload --port 8000
```

---

### ✅ Step 6: Run the Frontend (Streamlit or React)

For **Streamlit** UI:

```bash
streamlit run streamlit_app.py
```

For **React** frontend:

```bash
cd frontend
npm install
npm start
```


---

## 👨‍💻 Author

Made with ❤️ by [Aniruddha Shit](https://github.com/Aniru18)

---

## 📸 Screenshots

### 🔷 Streamlit Interface

![Streamlit UI](./assets/streamlit.jpg)

---

### 🟦 React Frontend Interface

![React UI](./assets/react.jpg)


