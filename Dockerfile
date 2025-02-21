FROM python:3.12
LABEL maintainer="osidiv@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
