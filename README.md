# Sensor Monitoring System (Python + FastAPI + SQLAlchemy)

A real-time simulated industrial sensor monitoring backend built using FastAPI and SQLite.

## Features

- Simulates temperature, pressure, and vibration sensor streams
- Stores live sensor telemetry into SQL database
- Detects abnormal sensor values using alert thresholds
- Provides REST API for retrieving latest sensor readings
- Background threaded data generation pipeline
- Swagger API documentation support

## Tech Stack

Python
FastAPI
SQLAlchemy
SQLite
Threading

## API Endpoints

GET / → System status

GET /sensors → Returns latest 20 sensor readings

## Example Output

{
  "sensor_name": "temperature",
  "sensor_value": 81.04,
  "timestamp": "2026-04-04T09:02:56"
}

## Use Case

This project simulates a lightweight industrial telemetry monitoring service similar to systems used in:

- factory automation
- predictive maintenance pipelines
- robotics monitoring
- IoT dashboards