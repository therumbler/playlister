FROM node:14.10 as builder

WORKDIR /build

COPY ./playlister-vue/ /build
RUN cd /build
RUN ls
RUN npm install
RUN npm run build

FROM python:3.8

RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
COPY . /app/
RUN mkdir /app/playlister-vue/dist
COPY --from=builder /build/dist/ /app/playlister-vue/dist
ENTRYPOINT ["./bin/docker-entrypoint.sh"]
