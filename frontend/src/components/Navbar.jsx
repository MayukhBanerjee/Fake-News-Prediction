import React from "react";
import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="nav">
      <div className="nav__brand">AI Fake News Detector</div>
      <nav className="nav__links">
        <a href="#dashboard">Dashboard</a>
        <a href="#analyze">Analyze</a>
        <a href="#about">About</a>
      </nav>
    </header>
  );
}
