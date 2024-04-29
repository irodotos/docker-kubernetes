FROM python:3.10.3-slim

RUN pip install Flask

COPY . /app
WORKDIR /app


ENV MESSAGE="hello from environment variable"

CMD python hello.py
