# Overtone Music Service (Assignment 4: Cloud Deployment)

This repository contains the Music Service, one of the core CRUD microservices for the Overtone project. The service is implemented using FastAPI (Python) and utilizes the motor driver for asynchronous connectivity with MongoDB Atlas.

The primary objective of this assignment was to successfully containerize and deploy this microservice to a cloud environment, demonstrating secure configuration and operational readiness.

## 🚀 Live Deployment Status

The application is deployed as a Docker-based Web Service on Render.com.

| Component             | URL                                                                                            | Status  | Verification Point                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------- |
| Live API Endpoint     | [https://overtone-music.onrender.com](https://overtone-music.onrender.com)                     | LIVE    | Base service status: {"status":"ok",...}                              |
| API Documentation     | [https://overtone-music.onrender.com/docs](https://overtone-music.onrender.com/docs)           | Active  | Interactive Swagger UI for all CRUD endpoints.                        |
| Database Health Check | [https://overtone-music.onrender.com/health/db](https://overtone-music.onrender.com/health/db) | SUCCESS | CRITICAL: {"status":"ok", "message":"Database connection successful"} |

## 📋 API Endpoints

The service provides CRUD operations for artists and tracks, along with system health checks.

| Method | Endpoint             | Description                                                        |
| ------ | -------------------- | ------------------------------------------------------------------ |
| GET    | /                    | Root endpoint to verify the service is running.                    |
| GET    | /health/db           | Assignment Requirement: Checks live connectivity to MongoDB Atlas. |
| GET    | /docs                | Displays the interactive Swagger UI documentation.                 |
| POST   | /artists             | Creates a new artist.                                              |
| GET    | /artists             | Retrieves a list of all artists.                                   |
| GET    | /artists/{artist_id} | Retrieves a single artist by their ID.                             |
| POST   | /tracks              | Creates a new track.                                               |
| GET    | /tracks              | Retrieves a list of all tracks.                                    |
| GET    | /tracks/{track_id}   | Retrieves a single track by its ID.                                |

## 📸 Deployment & Testing Screenshots

Follow the instructions provided here or simply drag-and-drop images into the GitHub editor to add screenshots.

1. Render Dashboard (Service is "Live")
2. Database Health Check (SUCCESS)
3. Swagger UI Documentation (/docs)
4. Successful POST Request (Testing Data Persistence)

## ⚙️ Technology Stack

| Category         | Technology                 | Purpose                                         |
| ---------------- | -------------------------- | ----------------------------------------------- |
| Framework        | FastAPI (Python 3.11)      | High-performance API foundation.                |
| Web Server       | Uvicorn                    | ASGI server for production deployment.          |
| Database         | MongoDB Atlas (M0 Cluster) | Cloud-hosted NoSQL database.                    |
| Driver           | motor                      | Asynchronous MongoDB driver.                    |
| Containerization | Docker                     | Packaging the application and its dependencies. |
| Deployment       | Render.com                 | Cloud platform for continuous deployment.       |

## 📂 Project Structure

```
music-service/
├── app/
│   ├── routes/
│   │   ├── artists.py  # CRUD routes for artist entities
│   │   └── tracks.py   # CRUD routes for track entities
│   ├── database.py     # Configuration for secure MongoDB connection via ENV vars
│   ├── main.py         # Main FastAPI application instance and health check endpoint
│   └── models.py       # Pydantic models for data validation/serialization
├── Dockerfile          # Container build instructions
└── requirements.txt    # Python dependency list
```

## 🔒 Security and Configuration (Task 3 & 4)

### 1. Environment Variables

All sensitive data is injected into the running container via Render's Environment Variables interface, ensuring the source code remains free of secrets.

| Variable   | Description                     | Security Note             |
| ---------- | ------------------------------- | ------------------------- |
| MONGO_URI  | MongoDB Atlas connection string | Securely stored on Render |
| DB_NAME    | Database name (`music`)         | Securely stored on Render |
| JWT_SECRET | Secret key for authentication   | Securely stored on Render |

### 2. TLS/SSL Troubleshooting (Task 4)

To resolve TLS certificate trust issues when connecting to MongoDB Atlas, the Dockerfile was updated to install required system certificates:

```
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*
```

Additionally, the MongoDB Atlas Network Access List was configured to allow connections from Render's dynamic IP range (`0.0.0.0/0`).

## 🏥 Health Endpoint Implementation

The `/health/db` endpoint executes a safe `client.admin.command('ping')` request to validate live database connectivity. If the check fails, it returns HTTP 500 with diagnostic logging, meeting assignment reliability and error-handling criteria.

DB Screenshots:
<img width="1895" height="775" alt="image" src="https://github.com/user-attachments/assets/a551b367-453f-40b6-90e3-f83564012516" />
<img width="1898" height="796" alt="image" src="https://github.com/user-attachments/assets/21bda73c-5491-46bf-9e9a-232bf6a07897" />


