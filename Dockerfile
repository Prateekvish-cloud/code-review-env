FROM python:3.10

WORKDIR /app

COPY . .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (HF uses 7860)
EXPOSE 7860

# Run FastAPI server
CMD ["python", "server/app.py"]