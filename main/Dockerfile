FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . /app

CMD python main.py