FROM python:3.10-slim

# Install system dependencies for audio
RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir faster-whisper sounddevice scipy requests

# Copy the rest of the app
COPY . .

# Default command
CMD ["python", "backend/main.py"]
