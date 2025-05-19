# Use a specific Python version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the files we need
COPY app.py requirements.txt ./

# Install dependencies directly
RUN pip install --no-cache-dir -r requirements.txt

# Install tenacity at the specific version to resolve conflicts
RUN pip install --no-cache-dir --force-reinstall tenacity==9.2.2

# Expose port
EXPOSE 8000

# Start command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
