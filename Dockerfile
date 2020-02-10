FROM python:3.6-slim-buster

ENV APP_DIR=/app
ENV PYTHON_VENV=$APP_DIR/.venv

WORKDIR /app/src
COPY src/ .
RUN python -m venv $PYTHON_VENV \
    && $PYTHON_VENV/bin/python -m pip install -r requirements.txt --upgrade pip \
    && chmod -R a+u /app

ENV PATH="$PYTHON_VENV/bin:$PATH"
