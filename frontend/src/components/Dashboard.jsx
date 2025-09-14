import React from "react";
import OutputWindow from "./OutputWindow";
import "./Dashboard.css";

export default function Dashboard({ result, isLoading }) {
  return (
    <section className="dash">
      {isLoading ? (
        <div className="dash__card dash__loading">
          <h2>Performing Dual Analysis...</h2>
          <p>Contacting Gemini Agent. This may take a moment.</p>
          <div className="spinner" />
        </div>
      ) : result ? (
        <div className="dash__card dash__result">
          <OutputWindow result={result} />
        </div>
      ) : (
        <div className="dash__card dash__placeholder">
          <h2>Your Analysis Results Will Appear Here</h2>
          <p>Paste an article into the form below to begin.</p>
        </div>
      )}
    </section>
  );
}
