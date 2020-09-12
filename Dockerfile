FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . /app/

ENTRYPOINT ["./bin/docker-entrypoint.sh"]