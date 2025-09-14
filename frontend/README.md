<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Fake News Detector Showcase</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        :root {
            --dark-bg: #1a1a1a;
            --primary-blue: #3498db;
            --card-bg: #2c3e50;
            --text-light: #ecf0f1;
            --text-muted: #95a5a6;
            --accent-green: #2ecc71;
            --accent-red: #e74c3c;
        }
        html {
            scroll-behavior: smooth;
        }
        body {
            background-color: var(--dark-bg);
            color: var(--text-light);
            font-family: 'Inter', sans-serif;
            margin: 0;
            line-height: 1.6;
        }
        .container {
            max-width: 960px;
            margin: 0 auto;
            padding: 2rem;
        }
        header {
            text-align: center;
            padding: 4rem 0;
            border-bottom: 1px solid var(--card-bg);
        }
        header h1 {
            font-size: 3.5rem;
            font-weight: 900;
            margin: 0;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }
        header p {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 600px;
            margin: 1rem auto 0;
        }
        section {
            padding: 4rem 0;
        }
        h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--primary-blue);
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }
        .card {
            background-color: var(--card-bg);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        }
        .card h3 {
            margin-top: 0;
            font-size: 1.8rem;
        }
        .card strong {
            color: var(--primary-blue);
        }
        .feature-list {
            list-style: none;
            padding: 0;
        }
        .feature-list li {
            background-color: var(--card-bg);
            margin-bottom: 1rem;
            padding: 1.2rem;
            border-radius: 10px;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
        }
        .feature-list li::before {
            content: '✨';
            font-size: 1.5rem;
            margin-right: 1rem;
        }
        .tech-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
        }
        .tech-pill {
            background-color: var(--card-bg);
            color: var(--text-light);
            padding: 0.5rem 1.2rem;
            border-radius: 20px;
            font-weight: bold;
        }
        .code-block {
            background-color: #161b22;
            border: 1px solid var(--card-bg);
            border-radius: 10px;
            padding: 1.5rem;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
            white-space: pre;
        }
        footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
            border-top: 1px solid var(--card-bg);
            color: var(--text-muted);
        }
        @media (max-width: 768px) {
            .grid {
                grid-template-columns: 1fr;
            }
            header h1 {
                font-size: 2.5rem;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <header data-aos="fade-in">
            <h1>🤖 AI Fake News Detector</h1>
            <p>An advanced, explainable AI system designed to combat misinformation by leveraging a unique dual-model analysis.</p>
        </header>

        <section id="how-it-works" data-aos="fade-up">
            <h2>💡 How It Works: The Dual-Model Engine</h2>
            <div class="grid">
                <div class="card" data-aos="fade-right" data-aos-delay="100">
                    <h3>The Specialist: ML Model 🐾</h3>
                    <p>A classic <strong>Logistic Regression</strong> model trained on a large dataset. It's incredibly fast and efficient, acting as the first line of analysis.</p>
                    <p><strong>Output:</strong> Provides a lightning-fast "Real" or "Fake" verdict and a quantifiable <strong>confidence score</strong>.</p>
                </div>
                <div class="card" data-aos="fade-left" data-aos-delay="200">
                    <h3>The Generalist: Gemini Agent 🕵️</h3>
                    <p>A powerful <strong>Large Language Model (Google Gemini)</strong> that understands context, nuance, and subtlety. It acts as an expert consultant for a deep, reason-based analysis.</p>
                    <p><strong>Output:</strong> Provides an independent verdict and a list of <strong>key phrases</strong> that justify its decision (Explainable AI).</p>
                </div>
            </div>
        </section>

        <section id="features" data-aos="fade-up">
            <h2>✨ Key Features</h2>
            <ul class="feature-list">
                <li data-aos="fade-left">Combines the speed of traditional ML with the reasoning power of a cutting-edge LLM.</li>
                <li data-aos="fade-left" data-aos-delay="100">Highlights the specific phrases that influenced the agent's verdict for full transparency.</li>
                <li data-aos="fade-left" data-aos-delay="200">Seamlessly analyze news by pasting raw text or by providing a URL for automatic scraping.</li>
                <li data-aos="fade-left" data-aos-delay="300">Asynchronous backend built with FastAPI handles concurrent analysis efficiently.</li>
            </ul>
        </section>

        <section id="tech-stack" data-aos="fade-up">
            <h2>🛠️ Technology Stack</h2>
            <div class="tech-grid">
                <span class="tech-pill" data-aos="zoom-in">Python</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="50">FastAPI</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="100">scikit-learn</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="150">Google Gemini</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="200">React</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="250">Axios</span>
                <span class="tech-pill" data-aos="zoom-in" data-aos-delay="300">AOS</span>
            </div>
        </section>

        <section id="getting-started" data-aos="fade-up">
            <h2>🚀 Getting Started</h2>
            <h3>Backend Setup</h3>
            <div class="code-block" data-aos="fade-up">
# Install dependencies
pip install -r requirements.txt

# Create .env file and add API key
echo "GEMINI_API_KEY=your_google_gemini_api_key" > .env

# Run the server
uvicorn main:app --reload --timeout-keep-alive 120
            </div>
            <h3 style="margin-top: 2rem;">Frontend Setup</h3>
            <div class="code-block" data-aos="fade-up">
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm start
            </div>
        </section>
        
        <footer>
            <p>Powered by the Google Gemini API &bull; Dataset from Kaggle</p>
        </footer>
    </div>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            once: true,
            duration: 800,
        });
    </script>
</body>
</html>
