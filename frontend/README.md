🤖 AI Fake News Detector
An advanced, explainable AI system designed to combat misinformation by leveraging a unique dual-model analysis. This project combines a high-speed, pattern-based Machine Learning model with the deep contextual reasoning of Google's Gemini agent to provide nuanced and transparent verdicts on news articles.

(Suggestion: Record a short GIF of your app in action and replace the link above)

💡 How It Works: The Dual-Model AI Engine
This isn't just another fake news detector. It's an ensemble system that gets the best of two different AI approaches, much like pairing a highly trained sniffer dog with a seasoned detective.

1. The Specialist: The ML Model 🐾
A classic Logistic Regression model trained on a large dataset of real and fake news. It's incredibly fast and efficient.

Role: Acts as the first line of analysis.

Strength: Rapidly detects statistical patterns, word frequencies (TF-IDF), and linguistic structures common in fake news.

Output: Provides a lightning-fast "Real" or "Fake" verdict and a quantifiable confidence score (e.g., 98% confident).

2. The Generalist: The Gemini Agent 🕵️
A powerful, generalist Large Language Model (Google Gemini) that understands context, nuance, and subtlety.

Role: Acts as the expert consultant, performing a deep, reason-based analysis.

Strength: It's not limited to the training data. It uses its vast knowledge to scrutinize claims, analyze language for bias, and evaluate the article's overall context.

Output: Provides an independent "Real" or "Fake" verdict and, crucially, a list of key phrases that justify its decision, adding a layer of Explainable AI (XAI).

3. The Combined Verdict
The system intelligently combines the outputs of both models:

Agreement: If both models agree, the final verdict is presented with high certainty.

Disagreement: If the models return different verdicts, the system flags it as a "Conflicting Analysis." This is a key feature, as it transparently communicates that the article is nuanced and requires human judgment.

✨ Key Features
Hybrid AI Engine: Combines the speed of traditional ML with the reasoning power of a cutting-edge LLM.

Explainable AI (XAI): The Gemini agent highlights the specific words and phrases that influenced its verdict, making the results transparent and trustworthy.

URL & Text Analysis: Seamlessly analyze news by pasting raw text or by providing a URL, which the system will automatically scrape and analyze.

Robust Backend: Built with FastAPI, the asynchronous backend handles concurrent analysis of both models efficiently, even under load.

Modern & Responsive UI: A fluid and intuitive frontend built with React, featuring smooth animations and a clear, color-coded results dashboard.

🛠️ Technology Stack
Backend: Python, FastAPI, scikit-learn, Google Generative AI, Newspaper3k

Frontend: React, Axios, AOS (for animations), Validator.js

AI/ML: Logistic Regression, TF-IDF Vectorization, Google Gemini 1.5 Pro

🚀 Getting Started
1. Prerequisites
Python 3.8+ and Node.js v16+

A Google Gemini API key. You can get one from the Google AI Studio.

2. Clone & Setup
Bash

# Clone the repository
git clone https://github.com/yourusername/ai-fake-news-detector.git
cd ai-fake-news-detector/Hackathon
3. Backend Setup
Bash

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install Python dependencies
pip install -r requirements.txt

# Create a .env file and add your API key
echo "GEMINI_API_KEY=your_google_gemini_api_key" > .env

# Run the backend server (with an increased timeout for AI calls)
uvicorn main:app --reload --timeout-keep-alive 120
The API will be available at http://127.0.0.1:8000.

4. Frontend Setup
Bash

# Navigate to the frontend directory in a new terminal
cd frontend

# Install Node.js dependencies
npm install

# Run the React development server
npm start
The application will open at http://localhost:3000.

📖 Acknowledgements
This project was built on the Fake and Real News Dataset available on Kaggle.

Powered by the Google Gemini API.

Frontend bootstrapped with Create React App.
