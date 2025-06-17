# GovAim Intelligence Platform

GovAim is an AI-powered unified governance intelligence platform that combines real-time financial sentiment analysis and smart query interpretation for policy, fraud detection, and investment insights. The system integrates a GPT-backed chatbot (GovAim) with a Palantir-style dashboard for visual and contextual intelligence delivery.

---

## Features

- **Chatbot with GPT-3.5-Turbo:** Understands natural language queries related to governance, finance, fraud detection, and economic events.
- **FinBERT Sentiment Analysis:** Extracts financial sentiment (Positive/Negative/Neutral) from user queries in real time.
- **Real-time Query Interface:** Ask questions like "Run predictive fraud analysis" or "Summarize budget 2025."
- **Integrated Visual Intelligence (Palantir Clone):** Enables interaction between textual insights and analytical dashboards.
- **Unified Frontend & Backend Stack:** Seamless integration between React and Django with REST APIs.

---

## Tech Stack

### Backend (Django)
- Django 5.x
- Django REST Framework
- OpenAI SDK (chat completions)
- Transformers (FinBERT model)
- dotenv
- SQLite (dev) / PostgreSQL (optional)

### Frontend (React + Vite + Tailwind)
- React.js
- Vite
- Tailwind CSS
- Axios (for API calls)

---

## Project Structure

```
govaim-platform/
├── backend/
│   ├── manage.py
│   └── govaim_chat/            # Chatbot logic, FinBERT, GPT integration
├── frontend/
│   ├── src/
│   ├── App.jsx
│   └── services/api.js         # Axios calls to /api/chat/
```

---

## Setup Instructions

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

Create a `.env` file with your OpenAI key:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

Make sure your React app sends POST requests to:
```
http://127.0.0.1:8000/api/chat/
```

---

## API Overview

### POST `/api/chat/`
**Request Body:**
```json
{
  "query": "Summarize budget 2025"
}
```

**Response:**
```json
{
  "reply": "The 2025 budget focuses on capital expenditure, fiscal consolidation..."
}
```

---

## How It Works

- All POST requests to `/api/chat/` are routed to `chat_handler()`.
- If the query contains words like "sentiment", FinBERT is used.
- Otherwise, the query is handled by GPT-3.5 via the OpenAI API.
- React's frontend sends user input via Axios to Django API, and displays the response.

---

## Challenges Faced

- Integrating new OpenAI Python SDK (`openai>=1.0`) required adapting to client-based architecture.
- Cross-origin issues resolved via `django-cors-headers`.
- Managing latency and fallback handling for long GPT responses.

---

## Future Improvements

- Add authentication and user roles
- Save query history to database
- Deploy with Docker and CI/CD pipeline
- Integrate with a live data source (e.g., NSE/BSE APIs)
- Add voice-to-text input support

---

## License

This project is open for academic, research, or prototype use. Contact the maintainer for enterprise rights.
