import React, { useState } from 'react';
import validator from 'validator';
import './NewsForm.css';

export default function NewsForm({ onAnalyze, isLoading, error, setError }) {
  const [inputType, setInputType] = useState('text'); // "text" | "url"
  const [inputValue, setInputValue] = useState('');

  const validate = () => {
    if (inputType === 'url') {
      if (!validator.isURL(inputValue, { require_protocol: false })) {
        setError('Invalid URL! Please enter a valid news link.');
        return false;
      }
    } else {
      if (!inputValue.trim() || !/[a-zA-Z]/.test(inputValue)) {
        setError('Please paste news text containing letters.');
        return false;
      }
    }
    setError('');
    return true;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validate()) return;
    // IMPORTANT: delegate to parent so Dashboard (top box) shows the result
    onAnalyze(inputValue, inputType);
  };

  const handleTypeChange = (type) => {
    setInputType(type);
    setInputValue('');
    setError('');
  };

  return (
    <section className="news-form" id="analyze">
      <h2>Analyze News</h2>

      <div className="toggle-buttons">
        <button
          className={inputType === 'text' ? 'active' : ''}
          type="button"
          onClick={() => handleTypeChange('text')}
          disabled={isLoading}
        >
          Text
        </button>
        <button
          className={inputType === 'url' ? 'active' : ''}
          type="button"
          onClick={() => handleTypeChange('url')}
          disabled={isLoading}
        >
          URL
        </button>
      </div>

      <form onSubmit={handleSubmit}>
        {inputType === 'text' ? (
          <textarea
            rows={8}
            placeholder="Paste news text here..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            disabled={isLoading}
          />
        ) : (
          <input
            type="url"
            placeholder="Paste news URL here..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            disabled={isLoading}
          />
        )}

        {error && <div className="error">{error}</div>}

        <button type="submit" className="analyze-btn" disabled={isLoading}>
          {isLoading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>

      {/* NOTE: Do NOT render <OutputWindow /> here.
          The Dashboard (top box) is responsible for displaying results. */}
    </section>
  );
}
