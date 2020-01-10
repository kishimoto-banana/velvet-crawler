FROM python:3.8

COPY requirements.txt /crawler/
WORKDIR /crawler

RUN pip install -r ./requirements.txt
