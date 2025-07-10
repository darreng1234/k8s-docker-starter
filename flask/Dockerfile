FROM python:3.9-slim

WORKDIR /app
COPY flask/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "/app/flask/app.py"]