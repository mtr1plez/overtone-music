FROM python:3.11-slim

# MANDATORY STEP 4: Install system certificates for secure connection to MongoDB Atlas (TLS/SSL)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates openssl && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory contents
COPY ./app ./app

# Expose port (optional, but good practice)
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]