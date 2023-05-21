FROM python:3.9-alpine3.13

LABEL maintainer="BurakKocak99"

ENV PYTHONBUFFERED 1


COPY ./requirements.txt /requirements.txt
COPY ./StoriesPlatform /StoriesPlatform

WORKDIR /StoriesPlatform

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app

