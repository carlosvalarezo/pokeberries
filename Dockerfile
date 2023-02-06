FROM python:3.8-slim-buster AS dev

RUN apt update -y && apt upgrade -y

RUN useradd --user-group --system --create-home --no-log-init pythonuser

WORKDIR /api

RUN chown -R pythonuser:pythonuser /api \
    && chmod 755 /api

ADD requirements.txt /api
ADD requirements.dev.txt /api

USER pythonuser

RUN python -m pip install -r requirements.dev.txt


FROM dev AS run

ENTRYPOINT ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "main:app"]