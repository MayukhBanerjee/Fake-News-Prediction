// src/App.jsx
import React, { useState, useEffect } from 'react';

// Animation lib (optional, matches your earlier setup)
import AOS from 'aos';
import 'aos/dist/aos.css';

// Components
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import NewsForm from './components/NewsForm';
import About from './components/About';

// API helpers
import { fetchNewsAnalysis, fetchUrlAnalysis } from './api/detection';

// Styles
import './styles/main.css';

function App() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    AOS.init({ duration: 1000, once: true });
  }, []);

  /**
   * Handle both Text and URL analysis
   * @param {string} inputValue - text or url
   * @param {"text"|"url"} inputType
   */
  const handleAnalyze = async (inputValue, inputType = 'text') => {
    setResult(null);
    setError('');
    setIsLoading(true);

    // Always scroll user to the Dashboard (top box) where results appear
    document.getElementById('dashboard')?.scrollIntoView({ behavior: 'smooth' });

    try {
      const data =
        inputType === 'url'
          ? await fetchUrlAnalysis(inputValue)
          : await fetchNewsAnalysis(inputValue);

      setResult(data);
    } catch (err) {
      console.error(err);
      setError(
        'Analysis failed. The server may be busy or the request timed out. Please try again.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div id="home">
      <Navbar />

      <div className="app-container">
        <main className="main-content">
          {/* TOP: Results box (placeholder → loading → result) */}
          <section id="dashboard" data-aos="fade-up">
            <Dashboard result={result} isLoading={isLoading} />
          </section>

          {/* BELOW: Analyze form (Text / URL) */}
          <section id="analyze" data-aos="fade-up" data-aos-delay="150">
            <NewsForm
              onAnalyze={handleAnalyze}
              isLoading={isLoading}
              error={error}
              setError={setError}
            />
          </section>

          {/* BOTTOM: About developers */}
          <section id="about" data-aos="fade-up" data-aos-delay="200">
            <About />
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;
