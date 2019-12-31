FROM python:3.8

ADD requirements.txt /crawler/
WORKDIR /crawler

RUN pip install -r ./requirements.txt
