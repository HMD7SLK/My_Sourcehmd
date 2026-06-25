FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "YousefMusic"]
