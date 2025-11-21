import React from "react";

export default function LandingPage() {
  return (
    <div className="landing-page landing-bg">
      <div className="landing-card">
        <span className="landing-logo">🚗</span>
        <h2 className="landing-title">Welcome!</h2>
        <p className="landing-desc">
          <strong>Explore accident data, get risk predictions, and visualize safety insights.</strong>
        </p>

        <div className="landing-actions">
          <a href="/dashboard" className="viz-btn landing-btn">Go to Dashboard</a>
          <a href="/predict" className="nav-btn landing-btn" style={{marginLeft:"1rem"}}>Predict Severity</a>
        </div>
      </div>
    </div>
  );
}

