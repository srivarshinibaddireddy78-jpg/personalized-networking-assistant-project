# 🤝 Personalized Networking Assistant

An AI-powered networking assistant that helps users generate personalized conversation starters by analyzing networking event descriptions using Natural Language Processing (NLP).

Built using **FastAPI**, **Streamlit**, **Transformers (NLP)**, **Wikipedia API**, and **ReportLab**.

---

# 📌 Features

- 🔍 Analyze networking event descriptions
- 🧠 Detect important topics using NLP
- 💬 Generate personalized conversation starters
- 🌐 Verify topics using Wikipedia API
- 📜 Save conversation history
- 👍👎 Collect user feedback
- 📄 Download conversation reports as PDF
- 🧪 Unit testing using PyTest
- 📘 Interactive API documentation using Swagger UI

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Streamlit Frontend
                  │
                  ▼
           FastAPI Backend
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
 Event Analyzer  Topic Generator
        │         │
        ▼         ▼
 Fact Checker   History Logger
        │
        ▼
 Wikipedia API + JSON Storage
```

---

# 📂 Project Structure

```
Personalized-Networking-Assistant/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routers/
│   └── services/
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   ├── test_routes.py
│   ├── test_event_analyzer.py
│   ├── test_fact_checker.py
│   └── conftest.py
│
├── images/
├── history.json
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| Transformers | NLP Processing |
| Wikipedia API | Fact Verification |
| ReportLab | PDF Generation |
| PyTest | Unit Testing |
| Git & GitHub | Version Control |

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/srivarshinibaddireddy78-jpg/Personalized-Networking-Assistant-Project.git
```

```bash
cd Personalized-Networking-Assistant-Project
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
python -m streamlit run frontend/streamlit_app.py
```

Frontend:

```
http://localhost:8501
```

---

# 🧪 Running Tests

Run all test cases:

```bash
pytest -v
```

Example Output

```
==================== 5 passed ====================
```

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home Page](app/images/home_page.png)
---

## 📝 Event Analysis

![Event Analysis](app/images/event_analysis.png)

---

## 💬 Conversation Starters

![Conversation Starters](app/images/conversation_starters.png)

---

## 🌐 Fact Checker

![Fact Checker](app/images/fact_checker.png)

---

## 📄 Swagger Documentation

![Swagger Documentation](app/images/swagger_docs.png)

---

## 📚 Conversation History

![Conversation History](app/images/conversation_history.png)

---
# 🧪 Running Tests

Example Output

![Test Results](appimages/test_results.png)

# 🔮 Future Enhancements

- 🤖 Gemini API Integration
- 🔐 User Authentication
- ☁️ Cloud Deployment
- 🗄️ Database Integration (MongoDB/PostgreSQL)
- 📊 Analytics Dashboard
- 🌙 Dark Mode Support

---

# 👩‍💻 Author

**Sri Varshini Baddireddy**

Google Generative AI Internship

GitHub:

https://github.com/srivarshinibaddireddy78-jpg/Personalized-Networking-Assistant-Project

---

# 📜 License

This project was developed as part of the Google Generative AI Internship for educational purposes.