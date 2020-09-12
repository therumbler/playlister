FROM python:3.8

RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . /app/

ENTRYPOINT ["./bin/docker-entrypoint.sh"]