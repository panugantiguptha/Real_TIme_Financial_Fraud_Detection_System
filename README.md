# Real-Time Credit Card Fraud Detection

This capstone project pairs a Python-based anomaly-detection pipeline with a React/Redux dashboard for viewing simulated transaction activity.

## Project structure

| Directory | Purpose |
| --- | --- |
| `fraud_detection_system/` | Trains an Isolation Forest model from transaction data and streams records through it, printing fraud alerts for anomalous transactions. |
| `Credit-Card-Fraud-Detection-Realtime-master/` | React/Redux dashboard with maps, charts, transaction views, and an Express server that supplies mock transaction data. |

## Features

- Isolation Forest anomaly detection with feature scaling
- Simulated, sequential transaction processing
- Console alerts for suspected fraudulent activity
- Interactive dashboard with maps, charts, table pagination, and clustered markers
- Express mock API for dashboard development

## Prerequisites

- Python 3.10 or later
- Node.js and npm (the dashboard uses older React/Webpack dependencies, so an LTS Node release is recommended)

## Run the fraud-detection pipeline

From the repository root:

```bash
cd fraud_detection_system
python -m pip install -r requirements.txt
python main.py
```

`main.py` retrains the model using `data/transaction_data.csv`, saves the artifacts in `models/`, then processes each transaction. Suspected anomalies are printed to the console.

You can also run each stage independently:

```bash
python train_model.py
python stream_simulator.py
```

## Run the dashboard

Open a second terminal from the repository root:

```bash
cd Credit-Card-Fraud-Detection-Realtime-master
npm install
node server.js
```

Then visit [http://localhost:8081](http://localhost:8081). The Express server provides mock endpoints at:

- `/api/transactions_map`
- `/api/region_query`

For front-end development with Webpack's development server, run:

```bash
npm start
```

## Data and model artifacts

The Python pipeline reads `fraud_detection_system/data/transaction_data.csv`. It uses numeric fields in that file to train the model and writes these generated artifacts:

- `fraud_detection_system/models/fraud_model.pkl`
- `fraud_detection_system/models/scaler.pkl`

## Notes

- The dashboard currently uses randomly generated mock API data; it is not directly connected to the Python pipeline.
- Alerts are printed locally by `alert_handler.py`. That module is a natural integration point for email, SMS, Kafka, or another notification service.

## License

No license has been specified for this repository.
