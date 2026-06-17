FROM python:3-alpine

COPY requirements.txt /temp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip pip install -r /temp/requirements.txt

COPY django /app
COPY init.sh /app/

WORKDIR /app

CMD ["/app/init.sh"]