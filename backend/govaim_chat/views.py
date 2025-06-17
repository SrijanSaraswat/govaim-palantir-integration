from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import torch
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# ✅ Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

# ✅ Load FinBERT model once at startup
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    labels = ['Negative', 'Neutral', 'Positive']
    sentiment = labels[probs.argmax()]
    return sentiment

@api_view(['POST'])
def chat_handler(request):
    query = request.data.get('query', '').strip()

    if not query:
        return Response({'reply': '⚠️ Empty query received.'})

    # ✅ Handle financial sentiment
    if "sentiment" in query.lower():
        sentiment = analyze_sentiment(query)
        return Response({'reply': f"Financial sentiment: {sentiment}"})

    # ✅ GPT-3.5 Turbo response
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        answer = response.choices[0].message.content.strip()
        return Response({'reply': answer})

    except Exception as e:
        return Response({'reply': f"❌ Error: {str(e)}"})
