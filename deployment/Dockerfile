FROM python:3.13-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /guilds
COPY . .

ENV DJANGO_SETTINGS_MODULE=auth_service.app.settings

CMD ["gunicorn", "auth_service.app.wsgi:application", "--bind", "0.0.0.0:8000"]

RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8



