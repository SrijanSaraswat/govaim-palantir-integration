# GovAim Intelligence Platform

GovAim is an AI-powered unified governance intelligence platform that combines real-time financial sentiment analysis and smart query interpretation for policy, fraud detection, and investment insights. The system integrates a GPT-backed chatbot (GovAim) with a Palantir-style dashboard for visual and contextual intelligence delivery.

---

## ✨ Features

- 🤖 **Chatbot with GPT-3.5-Turbo** – Understands natural language queries like policy analysis, budget summary, and fraud detection.
- 📊 **FinBERT Sentiment Analysis** – Extracts Positive/Neutral/Negative tone from financial user queries.
- 🔍 **Smart Query Detection** – Automatically classifies if the query is a sentiment-based task or GPT-based query.
- 🧠 **Unified Frontend + Backend** – Real-time data interaction from React to Django API.
- 📈 **Palantir-style Integration** – Allows GovAim chatbot to interact with a visual intelligence dashboard.

---

## ⚙️ Tech Stack & Tools

<p align="center">
  <img src="https://img.shields.io/badge/-Python-black?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Django%20REST%20Framework-grey?style=flat&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/-OpenAI-412991?style=flat&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Transformers-yellow?style=flat&logo=huggingface&logoColor=black"/>
  <br/>
  <img src="https://img.shields.io/badge/-React-20232A?style=flat&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/-Vite-646CFF?style=flat&logo=vite&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Tailwind-06B6D4?style=flat&logo=tailwind-css&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Axios-5A29E4?style=flat"/>
  <img src="https://img.shields.io/badge/-Node.js-339933?style=flat&logo=nodedotjs&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white"/>
</p>

---

## 📁 Project Structure

```
govaim-palantir-integration/
├── backend/
│   ├── analyses/
│   ├── connections/
│   ├── govaim_chat/
│   ├── workflows/
│   ├── astraeus_platform/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx, main.jsx, index.css...
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
```

---

## 🚀 Quick Start

### Backend (Django)
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Add your `.env` file:**
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

Ensure your React app posts queries to:
```
http://127.0.0.1:8000/api/chat/
```

---

## 💡 How It Works

- `/api/chat/` receives POST queries.
- If the query involves sentiment, it invokes FinBERT.
- Otherwise, OpenAI GPT processes the response.
- React frontend sends API requests via Axios and updates response on screen.

---

## 🛠️ Challenges Solved

- Migrated to OpenAI v1.0 Python SDK (breaking changes from old versions)
- Handled CORS errors via `django-cors-headers`
- Fixed broken pipeline errors and timeout issues with JSON payloads
- Created a single GitHub repo with unified backend + frontend folders

---

## 📌 Note

This project is structured for academic, hackathon, or early-stage production use. For enterprise scalability, consider Docker, PostgreSQL, and deployment on platforms like Render, Vercel, or Railway.
