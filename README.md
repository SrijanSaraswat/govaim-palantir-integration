
# 🚀 GovAim Intelligence Platform

GovAim is an AI-powered governance intelligence system that fuses real-time financial sentiment analysis and GPT-backed chat capabilities — all unified with a Palantir-style visual dashboard.

🔍 Whether it's fraud detection, policy analysis, or economic event insights — **GovAim** lets you ask *natural language* questions and get structured, intelligent answers.

---

## ✨ Features

- 🤖 **GPT-3.5 Chatbot:** Understands complex governance/finance queries.
- 📊 **FinBERT Sentiment Analysis:** Analyzes financial tone in real time.
- ⚙️ **Query Examples:** “Run predictive fraud analysis” / “Summarize Budget 2025.”
- 🧠 **Palantir-Inspired Dashboard:** Visual + contextual insights combined.
- 🔗 **Unified Full Stack Integration:** Django + React via REST APIs.

---

## 🛠️ Tech Stack & Tools

<p align="center">
  <img src="https://img.shields.io/badge/-C-659ad2?style=flat&logo=c&logoColor=white"/>
  <img src="https://img.shields.io/badge/-C++-00599C?style=flat&logo=c%2B%2B&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Python-black?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Solidity-363636?style=flat&logo=solidity&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Django%20REST%20Framework-grey?style=flat&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/-MySQL-F29111?style=flat&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/-PL/SQL-F80000?style=flat&logo=oracle&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/-JavaScript-F0DB4F?style=flat&logo=javascript&logoColor=black"/>
  <br/>
  <img src="https://img.shields.io/badge/-Git-F1502F?style=flat&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Postman-FF6C37?style=flat&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visual%20studio%20code&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/-Figma-000000?style=flat&logo=figma&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Adobe%20Illustrator-FF9A00?style=flat&logo=adobe-illustrator&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Adobe%20Photoshop-31A8FF?style=flat&logo=adobe-photoshop&logoColor=white"/>
</p>

---

## 🗂️ Project Structure

```
govaim-platform/
├── backend/
│   ├── manage.py
│   └── govaim_chat/          # Handles FinBERT + GPT logic
├── frontend/
│   ├── src/
│   ├── App.jsx
│   └── services/api.js       # Axios POST to /api/chat/
```

---

## ⚙️ Setup Instructions

### 🔁 Backend (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

✅ Create `.env` in the backend root:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 💻 Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

🧠 Make sure Axios points to:
```
http://127.0.0.1:8000/api/chat/
```

---

## 📡 API Overview

### POST `/api/chat/`

**Request Body:**
```json
{
  "query": "Summarize budget 2025"
}
```

**Sample Response:**
```json
{
  "reply": "The 2025 budget focuses on capital expenditure, fiscal consolidation..."
}
```

---

## 🧠 How It Works

1. **Frontend (React)** sends a POST request to `/api/chat/` via Axios.
2. **Backend (Django)** receives the query:
   - If it includes the word “sentiment” → analyzed using FinBERT.
   - Else → passed to GPT-3.5 via OpenAI SDK.
3. Response is sent back and rendered in the chat interface.

---

## 👥 Maintainer

Made with ❤️ by [@SrijanSaraswat](https://github.com/SrijanSaraswat)

For academic, research, and prototype use. Contact for enterprise licensing.
