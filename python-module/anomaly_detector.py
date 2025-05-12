from flask import Flask, jsonify, request
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

def load_and_preprocess(file_path):
    # Load CSV data; expected columns: event_id, timestamp, source, description
    df = pd.read_csv(file_path)
    # Convert timestamp to datetime and then to UNIX time for numeric analysis
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['unix_time'] = df['timestamp'].astype('int64') // 10**9
    # For this demo, only use the unix_time as a feature.
    features = df[['unix_time']]
    return df, features

@app.route('/detect', methods=['GET'])
def detect_anomalies():
    df, X = load_and_preprocess("python-module/data/siem_logs_sample.csv")
    
    # Apply IsolationForest; -1 indicates anomaly.
    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly_label'] = model.fit_predict(X)
    
    anomalies = df[df['anomaly_label'] == -1]
    result = anomalies[['event_id', 'timestamp', 'source', 'anomaly_label']].to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    # Run the Flask API on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
