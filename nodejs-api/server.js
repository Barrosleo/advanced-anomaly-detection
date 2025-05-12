// nodejs-api/server.js

const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files from the 'views' directory
app.use(express.static(path.join(__dirname, 'views')));

// API endpoint for fetching anomalies from the Python service
app.get('/api/anomalies', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/detect');
        let anomalies = response.data;
        // Add risk evaluation; here an anomaly (-1 label) is tagged 'High Risk'
        anomalies = anomalies.map(anomaly => ({
            ...anomaly,
            risk: anomaly.anomaly_label === -1 ? 'High Risk' : 'Normal'
        }));
        res.json(anomalies);
    } catch (err) {
        res.status(500).json({ error: 'Error fetching anomaly data.' });
    }
});

// Serve the dashboard page
app.get('/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'dashboard.html'));
});

app.listen(PORT, () => {
    console.log(`Node.js API running at http://localhost:${PORT}`);
});
