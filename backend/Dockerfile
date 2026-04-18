# # Use lightweight Python image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app

# # Prevent Python from writing pyc files
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first (better caching)
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Copy application code
# COPY ./app ./app

# # Expose FastAPI port
# EXPOSE 8000

# # Run FastAPI using Uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files & enable logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app ./app

# Expose port (IMPORTANT: match docker-compose & nginx)
EXPOSE 5000

# Run FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

