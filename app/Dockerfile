# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
# Use apk to install libpq-dev
RUN apk update && apk add --no-cache \
    postgresql-dev \
    postgresql-client \
    && rm -rf /var/cache/apk/*
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 


ENTRYPOINT ["/app/entrypoint.sh"]




