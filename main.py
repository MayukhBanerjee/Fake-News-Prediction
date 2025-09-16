""" import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import re # Import regex for cleaning

# --- Load Trained Model and Vectorizer ---
try:
    with open('robust_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('robust_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: robust_model.pkl or robust_vectorizer.pkl not found. Make sure they are in the same directory.")
    model = None
    vectorizer = None

# --- Function to clean text (should be the same as in train_model.py) ---
def preprocess_text(text):
    
    text = re.sub(r'^\w+\s*\([^)]*\)\s*-\s*', '', text, flags=re.IGNORECASE)
    return text.lower()

# --- Initialize the FastAPI app ---
app = FastAPI()

# --- CORS Middleware ---
origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Model for Request Body ---
class NewsArticle(BaseModel):
    text: str

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Fake News Detector API is running!"}

# --- CHANGED: URL now matches the frontend's request ---
@app.post("/analyze")
def analyze_news(article: NewsArticle): # Renamed function for clarity
    print(f"--- Received text for analysis: '{article.text}' ---")
    if not model or not vectorizer:
        return {"error": "Model not loaded. Cannot make predictions."}

    original_text = article.text
    processed_text = preprocess_text(original_text)
    
    vectorized_text = vectorizer.transform([processed_text])
    
    prediction = model.predict(vectorized_text)
    prediction_proba = model.predict_proba(vectorized_text)

    if prediction[0] == 0:
        result = "Fake"
        confidence = prediction_proba[0][0]
    else:
        result = "Real"
        confidence = prediction_proba[0][1]

    return {
        "prediction": result,
        "confidence": f"{confidence:.2f}"
    }

# --- This allows the script to be run directly ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

 """

import pickle
import uvicorn
import re
import os
import asyncio
import json
import requests
import numpy as np
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- Initial Setup ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    print("Gemini API configured successfully.")
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

try:
    with open('robust_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('robust_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    print("Fake news ML model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: ML models not found.")
    model = None
    vectorizer = None


# --- Asynchronous Gemini Helper Function ---
async def get_gemini_verdict(text: str):
    print("Requesting detailed verdict and justification from Gemini agent...")
    try:
        agent_model = genai.GenerativeModel('gemini-1.5-pro-latest')
        prompt = f"""
        *Act as an expert fact-checking journalist.*
        Your sole task is to analyze the following news article and determine its authenticity.
        *Follow these steps rigorously:*
        1. Analyze the article for claims, biased language, and overall context.
        2. Identify a list of 3 to 5 key words or short phrases that most strongly influenced your decision.
        3. Determine a final verdict of "Real" or "Fake".
        *Your Final Task:*
        Format your response as a single, valid JSON object with two keys:
        - "verdict": Your single-word verdict ("Real" or "Fake").
        - "justification_phrases": A JSON array of the 3-5 key phrases you identified.
        *Article Text to Analyze:*
        ---
        {text}
        ---
        """
        response = await agent_model.generate_content_async(prompt)
        response_text = response.text.strip().replace("```json", "").replace("```", "")
        data = json.loads(response_text)
        verdict = data.get("verdict", "Uncertain")
        phrases = data.get("justification_phrases", [])
        if verdict not in ["Real", "Fake"]:
            verdict = "Uncertain"
        print(f"Gemini agent verdict: {verdict}")
        return {"verdict": verdict, "phrases": phrases}
    except Exception as e:
        print(f"Error processing Gemini response: {e}")
        return {"verdict": "Error", "phrases": []}


# --- FastAPI App Setup ---
app = FastAPI(title="Explainable AI News Detector")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewsArticle(BaseModel):
    text: str


class UrlPayload(BaseModel):
    url: str


def preprocess_text(text):
    return re.sub(r'^\w+\s*\([^)]*\)\s*-\s*', '', text, flags=re.IGNORECASE).lower()


def fetch_url_text(url: str, timeout: float = 12.0) -> str:
    """Fetch and clean article text from a URL."""
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = "https://" + url
    except Exception:
        pass

    headers = {"User-Agent": "Mozilla/5.0 (NewsDetector/1.0)"}
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "form", "aside"]):
        tag.decompose()
    text = " ".join(soup.get_text(separator=" ").split())
    return text[:200000]  # cap size


def get_top_keywords(vectorizer, model, text, top_n=5):
    """Extract top high-weightage words from the ML model for a given text."""
    if not vectorizer or not model:
        return []

    vectorized = vectorizer.transform([text])
    feature_names = np.array(vectorizer.get_feature_names_out())

    # Get model coefficients for class 1 (Real vs Fake)
    coefs = model.coef_[0]

    # Multiply feature weights with TF-IDF values for this doc
    weighted = vectorized.toarray()[0] * coefs

    # Get top N indices
    top_indices = np.argsort(np.abs(weighted))[-top_n:][::-1]
    return feature_names[top_indices].tolist()


# --- Analyze Text Endpoint ---
@app.post("/analyze")
async def analyze_news(article: NewsArticle):
    if not model or not vectorizer:
        return {"error": "ML Model not loaded."}

    loop = asyncio.get_running_loop()

    def run_ml_model_in_thread():
        processed_text = preprocess_text(article.text)
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)[0]
        proba = model.predict_proba(vectorized_text)[0]
        keywords = get_top_keywords(vectorizer, model, processed_text)
        return prediction, proba, keywords

    ml_task = loop.run_in_executor(None, run_ml_model_in_thread)
    gemini_task = get_gemini_verdict(article.text)

    (ml_result, gemini_result) = await asyncio.gather(ml_task, gemini_task)

    ml_prediction_val, prediction_proba, keywords = ml_result
    ml_verdict = "Real" if ml_prediction_val == 1 else "Fake"
    ml_confidence = prediction_proba[1] if ml_prediction_val == 1 else prediction_proba[0]

    gemini_verdict = gemini_result["verdict"]
    justification_phrases = gemini_result["phrases"]

    if ml_verdict == gemini_verdict:
        final_verdict = ml_verdict
    elif gemini_verdict in ["Real", "Fake"]:
        final_verdict = "Conflicting Analysis"
    else:
        final_verdict = ml_verdict

    return {
        "final_verdict": final_verdict,
        "ml_verdict": ml_verdict,
        "ml_confidence": float(f"{ml_confidence:.2f}"),
        "gemini_verdict": gemini_verdict,
        "justification_phrases": justification_phrases,
        "highlighted_words": keywords,
    }


# --- Analyze URL Endpoint ---
@app.post("/analyze_url")
async def analyze_url(payload: UrlPayload):
    if not payload.url:
        return {"error": "Empty URL."}
    try:
        page_text = fetch_url_text(payload.url)
    except Exception as e:
        return {"error": f"Failed to fetch URL: {e}"}

    if not model or not vectorizer:
        gemini_result = await get_gemini_verdict(page_text)
        return {
            "final_verdict": gemini_result["verdict"],
            "ml_verdict": "Unavailable",
            "ml_confidence": None,
            "gemini_verdict": gemini_result["verdict"],
            "justification_phrases": gemini_result["phrases"],
            "highlighted_words": [],
            "source": payload.url,
            "note": "Local ML model/vectorizer not loaded.",
        }

    loop = asyncio.get_running_loop()

    def run_ml_model_in_thread():
        processed = preprocess_text(page_text)
        vect = vectorizer.transform([processed])
        pred = model.predict(vect)[0]
        proba = model.predict_proba(vect)[0]
        keywords = get_top_keywords(vectorizer, model, processed)
        return pred, proba, keywords

    ml_task = loop.run_in_executor(None, run_ml_model_in_thread)
    gemini_task = get_gemini_verdict(page_text)

    (ml_result, gemini_result) = await asyncio.gather(ml_task, gemini_task)

    pred_val, prediction_proba, keywords = ml_result
    ml_verdict = "Real" if pred_val == 1 else "Fake"
    ml_confidence = prediction_proba[1] if pred_val == 1 else prediction_proba[0]

    gemini_verdict = gemini_result["verdict"]
    justification_phrases = gemini_result["phrases"]

    if ml_verdict == gemini_verdict:
        final_verdict = ml_verdict
    elif gemini_verdict in ["Real", "Fake"]:
        final_verdict = "Conflicting Analysis"
    else:
        final_verdict = ml_verdict

    return {
        "final_verdict": final_verdict,
        "ml_verdict": ml_verdict,
        "ml_confidence": float(f"{ml_confidence:.2f}"),
        "gemini_verdict": gemini_verdict,
        "justification_phrases": justification_phrases,
        "highlighted_words": keywords,
        "source": payload.url,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


