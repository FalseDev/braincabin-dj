FROM python:slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 8000

EXPOSE $PORT

CMD ["python3", "manage.py", "runserver", "0.0.0.0:$PORT"]
