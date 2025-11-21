import React from "react";

export default function Dashboard() {
  return (
    <div className="dashboard-page">
      <h1 className="dashboard-title">Data Insights Dashboard</h1>

      <section className="chart-section">
        <h2 className="chart-title">Accident Severity Distribution</h2>
        <img src="http://localhost:5000/static_charts/severity_distribution.png" alt="Severity Distribution" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Top 10 Causes of Accidents</h2>
        <img src="http://localhost:5000/static_charts/top10_causes.png" alt="Top Causes" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Severity vs Top 10 Causes (Heatmap)</h2>
        <img src="http://localhost:5000/static_charts/heatmap_severity_cause.png" alt="Severity vs Causes Heatmap" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Severity by Light Conditions (Heatmap)</h2>
        <img src="http://localhost:5000/static_charts/heatmap_severity_light.png" alt="Severity by Light Heatmap" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Severity by Time Period</h2>
        <img src="http://localhost:5000/static_charts/time_period_severity.png" alt="Severity by Time" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Number of Casualties by Severity</h2>
        <img src="http://localhost:5000/static_charts/casualties_severity.png" alt="Casualties Severity" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Feature Importance (Top 15)</h2>
        <img src="http://localhost:5000/static_charts/feature_importance.png" alt="Feature Importance" className="chart-img"/>
      </section>

      <section className="chart-section">
        <h2 className="chart-title">Correlation Matrix</h2>
        <img src="http://localhost:5000/static_charts/corr_matrix.png" alt="Correlation Matrix" className="chart-img"/>
      </section>
    </div>
  );
}
