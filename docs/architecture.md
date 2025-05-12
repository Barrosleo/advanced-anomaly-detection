# Architecture & Design

## Overview
The **Advanced Anomaly Detection** system consists of three modular components:
1. **Python Module:**  
   - Ingests and preprocesses SIEM log data.
   - Uses IsolationForest for anomaly detection.
   - Exposes a REST API endpoint at `/detect`.

2. **Node.js API & Alerting Integration:**  
   - Calls the Python API to fetch anomaly data.
   - Adds risk evaluations and serves this data via its own endpoint.
   - Serves a static HTML dashboard.

3. **Visualization Dashboard:**  
   - Built with HTML and Plotly.js.
   - Fetches anomaly data via the Node.js API.
   - Displays anomalies on a timeline with risk annotations.

## Data Flow
- **Step 1:** Raw SIEM logs are loaded from `python-module/data/siem_logs_sample.csv`.
- **Step 2:** Timestamp conversion and feature extraction are performed.
- **Step 3:** An IsolationForest model identifies anomalies.
- **Step 4:** The results are made available via the `/detect` endpoint in Python.
- **Step 5:** The Node.js API calls this endpoint, assigns risk labels, and exposes `/api/anomalies`.
- **Step 6:** The front-end dashboard retrieves and displays the data with interactive visualizations.

## Future Enhancements
- Adding additional anomaly detection algorithms (e.g., clustering, autoencoders).
- Implementing automated alerting via email or Slack.
- Incorporating comprehensive logging and CI/CD pipelines for production readiness.
