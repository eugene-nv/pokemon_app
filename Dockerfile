FROM python:3.11.4-alpine3.17
COPY requirements.txt /temp/requirements.txt
COPY pokemon_app /pokemon_app

WORKDIR /pokemon
EXPOSE 8000

RUN pip install -r /temp/requirements.txt