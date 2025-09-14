# 🤖 AI Fake News Detector

An advanced, explainable AI system designed to combat misinformation by leveraging a unique **dual-model analysis**. This project combines a high-speed, pattern-based Machine Learning model with the deep contextual reasoning of Google's Gemini agent to provide nuanced and transparent verdicts on news articles.

---

### ✨ Live Demo

![AI Fake News Detector Demo](demo.gif)

---

### 💡 How It Works: The Dual-Model AI Engine

This isn't just another fake news detector. It's an ensemble system that gets the best of two different AI approaches, much like pairing a highly trained sniffer dog with a seasoned detective.

#### 1. The Specialist: The ML Model 🐾
A classic **Logistic Regression** model trained on a large dataset of real and fake news. It's incredibly fast and efficient.

-   **Role:** Acts as the first line of analysis.
-   **Strength:** Rapidly detects statistical patterns and word frequencies (TF-IDF) common in fake news.
-   **Output:** Provides a lightning-fast "Real" or "Fake" verdict and a quantifiable **confidence score**.

#### 2. The Generalist: The Gemini Agent 🕵️
A powerful, generalist **Large Language Model (Google Gemini)** that understands context, nuance, and subtlety.

-   **Role:** Acts as the expert consultant, performing a deep, reason-based analysis.
-   **Strength:** It uses its vast knowledge to scrutinize claims and analyze language for bias.
-   **Output:** Provides an independent verdict and, crucially, a list of **key phrases** that justify its decision, adding a layer of **Explainable AI (XAI)**.

#### 3. The Combined Verdict
The system intelligently combines the outputs of both models. If they disagree, it returns a **"Conflicting Analysis,"** transparently communicating that the article is nuanced and requires human judgment.

---

### 🛠️ Technology Stack

-   **Backend:** Python, FastAPI, scikit-learn, Google Generative AI, Newspaper3k
-   **Frontend:** React, Axios, AOS (for animations), Validator.js
-   **AI/ML:** Logistic Regression, TF-IDF Vectorization, Google Gemini 1.5 Pro

---

### 🚀 Getting Started

#### 1. Prerequisites
-   Python 3.8+ and Node.js v16+
-   A Google Gemini API key from the [Google AI Studio](https://ai.google.dev/).

#### 2. Clone & Setup
```bash
git clone [https://github.com/yourusername/ai-fake-news-detector.git](https://github.com/yourusername/ai-fake-news-detector.git)
cd ai-fake-news-detector/Hackathon