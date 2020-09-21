FROM nikolaik/python-nodejs:python3.8-nodejs12

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY staticsrc .
RUN npm i typescript --prefix staticsrc && npx tsc --prefix staticsrc

COPY . .

RUN python3 manage.py collectstatic --no-input
