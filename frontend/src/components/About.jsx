import React from 'react';
import './About.css';

export default function About() {
  const team = [
    { name: 'Mayukh Banerjee', role: 'Fullstack Developer' },
    { name: 'Shubham Kumar', role: 'Frontend Developer' },
    { name: 'Aryan Vinod', role: 'ML Developer' },
    { name: 'Harshit', role: 'ML Developer' },
    { name: 'Bharat', role: 'Frontend Developer' },
  ];

  return (
    <section id="about" className="about">
      <h2>About the Developers</h2>
      <div className="about__grid">
        {team.map((m, i) => (
          <div className="about__card" key={i}>
            <div className="about__name">{m.name}</div>
            <div className="about__role">{m.role}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
