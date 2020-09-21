FROM nikolaik/python-nodejs:python3.8-nodejs12

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY staticsrc .
RUN cd staticsrc/ && npm i && npm run-script build

COPY . .

RUN python3 manage.py collectstatic --no-input
