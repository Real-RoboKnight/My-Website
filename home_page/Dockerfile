FROM python:3-alpine

COPY requirements.txt /temp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

RUN python -m pip install Django
