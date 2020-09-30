FROM nikolaik/python-nodejs:python3.8-nodejs12

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN yarn --cwd staticsrc && yarn --cwd staticsrc build

RUN python3 manage.py collectstatic --no-input
