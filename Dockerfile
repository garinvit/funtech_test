FROM python:3.10-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql postgresql-client python3-dev musl-dev gcc bash libldap2-dev libsasl2-dev

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt