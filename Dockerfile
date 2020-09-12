FROM python:slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .