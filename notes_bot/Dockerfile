FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/main.py .
COPY src/producer.py .
COPY src/bot.py .
COPY src/db.py .
COPY src/settings.py .
CMD ["python", "main.py"]
