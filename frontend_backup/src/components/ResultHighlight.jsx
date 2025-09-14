import React from "react";
import "./ResultHighlight.css";

export default function ResultHighlight({ words = [] }) {
  if (!words || words.length === 0) return null;
  return (
    <div className="chips">
      {words.map((w, i) => (
        <span key={`${w}-${i}`} className="chip">{w}</span>
      ))}
    </div>
  );
}
