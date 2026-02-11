FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code and entry point
COPY . .


# Cloud Run expects the app to listen on the $PORT environment variable
#CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
