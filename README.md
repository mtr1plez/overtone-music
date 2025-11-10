# Overtone Music Service (Assignment 4: Cloud Deployment)

This repository contains the **Music Service**, one of the core CRUD microservices for the Overtone project. The service is implemented using **FastAPI** (Python) and utilizes the `motor` driver for asynchronous connectivity with **MongoDB Atlas**.

The primary objective of this assignment was to successfully containerize and deploy this microservice to a cloud environment, demonstrating secure configuration and operational readiness.

## 🚀 Live Deployment Status

The application is deployed as a **Docker-based Web Service** on **Render.com**.

| Component | URL | Status | Verification Point |
| :--- | :--- | :--- | :--- |
| **Live API Endpoint** | `https://overtone-music.onrender.com` | **LIVE** | Base service status: `{"status":"ok", "message":"Overtone Music Service is running"}` |
| **API Documentation (Swagger UI)** | `https://overtone-music.onrender.com/docs` | **Active** | Interactive documentation for all CRUD endpoints. |
| **Database Health Check** | `https://overtone-music.onrender.com/health/db` | **SUCCESS** | **CRITICAL:** Successfully connects to and pings MongoDB Atlas. |

## ⚙️ Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Framework** | FastAPI (Python 3.11) | High-performance API foundation. |
| **Web Server** | Uvicorn | ASGI server for production deployment. |
| **Database** | MongoDB Atlas (M0 Cluster) | Cloud-hosted NoSQL database. |
| **Driver** | `motor` | Asynchronous MongoDB driver. |
| **Containerization** | Docker | Packaging the application and its dependencies. |
| **Deployment** | Render.com | Cloud platform for continuous deployment. |

## 📂 Project Structure
music-service/
├── app/
│   ├── routes/
│   │   ├── artists.py    # CRUD routes for artist entities
│   │   └── tracks.py     # CRUD routes for track entities
│   ├── database.py       # Configuration for secure MongoDB connection via ENV vars
│   ├── main.py           # Main FastAPI application instance and health check endpoint
│   └── models.py         # Pydantic models for data validation/serialization
├── Dockerfile            # Container build instructions
└── requirements.txt      # Python dependency list

## 🔒 Security and Configuration (Task 3 & 4)

### 1. Environment Variables [cite: 31, 33, 34]

All sensitive data is injected into the running container via Render's **Environment Variables** interface, ensuring the source code remains free of secrets. The application is configured to read these variables using `os.getenv()`.

| Variable | Description | Security Note |
| :--- | :--- | :--- |
| `MONGO_URI` | The full MongoDB Atlas connection string (`mongodb+srv://...`). | **SECURELY STORED ON RENDER.** |
| `DB_NAME` | The target database name (`music`). | **SECURELY STORED ON RENDER.** |
| `JWT_SECRET` | A randomly generated secret key for authentication purposes. | **SECURELY STORED ON RENDER.** |

### 2. TLS/SSL Troubleshooting (Task 4) [cite: 36, 37]

A critical step for connecting Python images to MongoDB Atlas is ensuring system trust of SSL/TLS certificates. The initial connection attempt resulted in a `ServerSelectionTimeoutError`, often indicative of a networking or certificate issue.

The solution was to modify the **Dockerfile** to install the necessary system certificates:

```dockerfile
# MANDATORY STEP: Install ca-certificates and OpenSSL for secure (TLS/SSL) connection to MongoDB Atlas
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

Additionally, the MongoDB Atlas Network Access List was configured to include 0.0.0.0/0 to allow connections from Render's dynamic outbound IP pool.

🏥 Health Endpoint Implementation 

The required /health/db endpoint was implemented in app/main.py. This endpoint attempts to execute a non-intrusive database command (client.admin.command('ping')) to confirm live database connectivity. If the connection fails for any reason (e.g., wrong URI, network block), it raises an HTTP 500 error with a detailed log, fulfilling the error handling requirement.