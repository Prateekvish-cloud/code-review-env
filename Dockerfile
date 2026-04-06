FROM python:3.10

WORKDIR /app

# Copy all files
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir openai openenv-core

# Run inference
CMD ["python", "inference.py"]