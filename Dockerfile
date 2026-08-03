FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Set Python path
ENV PYTHONPATH=/app
ENV PORT=10000

EXPOSE 10000

CMD ["python", "backend/app.py"]
