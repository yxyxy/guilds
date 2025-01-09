FROM python:3.13-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /guilds
COPY . .

ENV DJANGO_SETTINGS_MODULE=auth_service.app.settings

CMD ["gunicorn", "auth_service.app.wsgi:application", "--bind", "0.0.0.0:8000"]

