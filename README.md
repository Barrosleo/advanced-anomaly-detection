# Advanced Anomaly Detection with Machine Learning

This project implements a multi-language system for advanced anomaly detection, reflecting cutting-edge SOC practices. It monitors SIEM log data using unsupervised machine learning techniques (e.g., IsolationForest) to flag abnormal behavior that might indicate zero-day threats or insider risks.

**Key Components:**
- **Data Preprocessing & Feature Extraction (Python):**  
  Cleans raw SIEM log data and extracts numerical features.
- **Anomaly Detection (Python):**  
  Uses an IsolationForest model to detect anomalies.
- **API Integration & Alerting (Node.js):**  
  Connects to the Python service, evaluates risk, and triggers an alerting mechanism.
- **Visualization Dashboard (HTML/JS):**  
  Displays anomalies and risk scores interactively using Plotly.js.

**Technology Stack:**  
Python, Node.js, JavaScript, HTML, Flask, Express, scikit-learn, Plotly.js

---

## Getting Started

### Prerequisites:
- Python 3.6+ and Node.js installed on your system.

### Installation:

1. **Python Module:**
   ```bash
   cd python-module
   pip install -r requirements.txt
   python anomaly_detector.py

The Python service will start on http://localhost:5000.

2. **Node.js API & Dashboard:**
cd ../nodejs-api
npm install
node server.js

The Node.js API (and dashboard) will be available at http://localhost:3000/dashboard.

**Architecture & Design
See the docs/architecture.md file for details on the design decisions, data flow, and integration of the multi-language components.

**License
This project is licensed under the MIT License.

** Repository Structure
advanced-anomaly-detection/
├── README.md
├── python-module/
│   ├── anomaly_detector.py      # Flask API & ML-based anomaly detection
│   ├── requirements.txt         # Python dependencies
│   └── data/
│       └── siem_logs_sample.csv # Sample SIEM log data
├── nodejs-api/
│   ├── server.js                # Express API & alert integration
│   ├── package.json             # Node.js dependencies
│   └── views/
│       └── dashboard.html       # HTML & Plotly.js dashboard
└── docs/
    └── architecture.md          # Detailed design and architecture explanation
