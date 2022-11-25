# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.7.14-slim-buster

LABEL maintaner="El Cidon"
LABEL author="Erick Fabiani <erickfabiani123@gmail.com>"

ENV PYTHONUNBUFFERED=1

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libxml2-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install wagtail==2.9.3

EXPOSE 8001