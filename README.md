# 🤝 Personalized Networking Assistant

An AI-powered networking assistant that helps users generate personalized conversation starters based on their interests and event details.

Built using FastAPI, Streamlit, NLP, and Google Gemini AI.

---

## 📌 Features

- Analyze user profiles and interests
- Generate personalized conversation starters
- Save conversation history
- User-friendly Streamlit interface
- FastAPI backend
- Google Gemini AI integration

---

# 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── Profile Analyzer
  ├── Conversation Generator
  ├── History Logger
  └── Gemini AI Integration
  │
  ▼
JSON Storage
```

---
```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── Profile Analyzer
  ├── Conversation Generator
  └── History Logger
  │
  ▼
Google Gemini AI
  │
  ▼
Generated Personalized Conversation
```

---

## 📂 Project Structure

```text
Personalized-Networking-Assistant/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── profile_analyzer.py
│   ├── conversation_generator.py
│   └── history_logger.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
├── images/
├── tests/
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/srivarshinibaddireddy78-jpg/GEN-AI-Personalized-Networking-Assistant-Project---Skillwallet.git

cd GEN-AI-Personalized-Networking-Assistant-Project---Skillwallet

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start FastAPI

```bash
uvicorn backend.main:app --reload
```

### Start Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini AI
- Natural Language Processing (NLP)
- Git
- GitHub

---

## 👩‍💻 Author

**Baddireddy Sri Varshini**

GitHub:
https://github.com/srivarshinibaddireddy78-jpg