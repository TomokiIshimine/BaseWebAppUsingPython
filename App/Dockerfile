FROM python:3.7

WORKDIR /app

RUN mkdir Source

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000