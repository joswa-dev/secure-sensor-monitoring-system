# Secure Sensor Monitoring System

A secure real-time sensor monitoring system built with FastAPI, JWT Authentication, WebSockets, Docker, and SQLite.

## Features

- User Registration & Login
- JWT Authentication
- Protected Sensor API
- Real-time Sensor Monitoring
- WebSocket Support
- SQLite Database
- Dockerized Application
- Docker Compose Support

## Tech Stack

- Python
- FastAPI
- SQLite
- JWT Authentication
- Docker
- Docker Compose
- WebSockets

## API Endpoints

### Authentication
- POST `/register`
- POST `/login`

### Protected Routes
- GET `/protected-sensors`

## Run Locally

### Clone Repository

```bash
git clone https://github.com/joswa-dev/secure-sensor-monitoring-system.git
cd secure-sensor-monitoring-system
```

### Run with Docker

```bash
docker compose up --build
```

### Open API Docs

```bash
http://localhost:8000/docs
```

## Example Login

```json
{
  "username": "admin",
  "password": "admin123"
}
```

## Project Status

✅ Completed  
✅ Dockerized  
✅ GitHub Ready

## Screenshots
Swagger API Docs running successfully

## Future Improvements
- Role-based access control
- Redis caching
- PostgreSQL migration
- Cloud deployment (AWS / Render)

## Author
Shibin Joswa
LinkedIn: https://www.linkedin.com/in/shibin-joswa-dev/
GitHub: https://github.com/joswa-dev