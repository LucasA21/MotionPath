# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.3

FROM python:${PYTHON_VERSION}-bookworm AS final

WORKDIR /app

COPY ./src/ .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD tail -f /dev/null
