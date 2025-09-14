// src/api/detection.js
import axios from 'axios';

// Point this to your FastAPI backend.
// You can override with an environment variable when deploying.
const API_URL = process.env.REACT_APP_API_BASE || 'http://127.0.0.1:8000';

/**
 * Send raw text to backend for analysis
 * @param {string} newsText
 * @returns {Promise<Object>}
 */
export async function fetchNewsAnalysis(newsText) {
  try {
    const res = await axios.post(
      `${API_URL}/analyze`,
      { text: newsText }, // backend expects { "text": "..." }
      {
        headers: { 'Content-Type': 'application/json' },
        timeout: 90000,
      }
    );
    return res.data;
  } catch (err) {
    console.error('Error fetching text analysis:', err);
    throw err;
  }
}

/**
 * Send a URL to backend for scraping + analysis
 * @param {string} newsUrl
 * @returns {Promise<Object>}
 */
export async function fetchUrlAnalysis(newsUrl) {
  try {
    const res = await axios.post(
      `${API_URL}/analyze_url`,
      { url: newsUrl }, // backend expects { "url": "..." }
      {
        headers: { 'Content-Type': 'application/json' },
        timeout: 90000,
      }
    );
    return res.data;
  } catch (err) {
    console.error('Error fetching URL analysis:', err);
    throw err;
  }
}
