import React from 'react';
import ResultHighlight from './ResultHighlight';
import './OutputWindow.css';

export default function OutputWindow({ result }) {
  if (!result) return null;

  const {
    final_verdict,
    ml_verdict,
    ml_confidence,
    gemini_verdict,
    justification_phrases = [],
    source
  } = result;

  const isFake = final_verdict === 'Fake';
  const isConflict = final_verdict === 'Conflicting Analysis';
  const confidencePct =
    typeof ml_confidence === 'number' ? (ml_confidence * 100).toFixed(0) : 'N/A';

  const cardClass =
    isConflict ? 'ow ow--conflict' : isFake ? 'ow ow--fake' : 'ow ow--real';

  return (
    <div className={cardClass}>
      <div className="ow__title">
        {isConflict ? 'CONFLICTING' : isFake ? 'FAKE' : 'REAL'}
      </div>

      {typeof ml_confidence === 'number' && (
        <>
          <div className="ow__label">ML Model Confidence:</div>
          <div className="ow__bar">
            <div className="ow__barFill" style={{ width: `${ml_confidence * 100}%` }} />
          </div>
          <div className="ow__barVal">{confidencePct}%</div>
        </>
      )}

      <div className="ow__pair">
        <div>ML Model<strong>{ml_verdict}</strong></div>
        <div>Gemini Agent<strong>{gemini_verdict}</strong></div>
      </div>

      {justification_phrases.length > 0 && (
        <>
          <div className="ow__sub">KEY PHRASES IDENTIFIED BY AGENT</div>
          <ResultHighlight words={justification_phrases} />
        </>
      )}

      <div className="ow__footer">
        {isConflict
          ? 'The models disagree. Manual verification is recommended.'
          : isFake
          ? 'Both models agree this content shows characteristics of misleading information.'
          : 'Both models agree this content appears to be genuine.'}
      </div>

      {source && (
        <div className="ow__source">
          Source:&nbsp;
          <a href={source} target="_blank" rel="noreferrer">
            {source}
          </a>
        </div>
      )}
    </div>
  );
}
