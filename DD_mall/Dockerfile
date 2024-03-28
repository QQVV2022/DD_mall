FROM python:3.9-alpine3.13
LABEL maintainer="Quinn"

ENV PYTHONUNBUFFERED 1

RUN mkdir app
COPY ./requirements.txt /app/DD_mall/requirements.txt
COPY ./DD_mall /app/DD_mall
COPY ./web /app/web

## production?
COPY scripts /scripts
WORKDIR /app/DD_mall

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base musl-dev linux-headers && \
    /py/bin/pip install -r requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    chown -R app:app /app && \
    chmod -R 755 /app/web && \
    chmod -R +x /scripts

## Create a user group 'xyzgroup'
#RUN addgroup -S xyzgroup
## Create a user 'app' under 'xyzgroup'
#RUN adduser -S -D -h /usr/app/src app xyzgroup
## Chown all the files to the app user.
#RUN chown -R app:xyzgroup /app/DD_mall

EXPOSE 8000

ENV PATH="/scripts:/py/bin:$PATH"

USER app

## production?
#CMD ["run.sh"]