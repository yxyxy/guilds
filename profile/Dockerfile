FROM python:3.13-slim

# Установим зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Настройка рабочей директории
WORKDIR /app

# Установим Poetry для управления зависимостями
RUN pip install poetry

# Копируем файлы проекта (пока пусто)
COPY . .

# Устанавливаем зависимости
RUN poetry install --no-dev

# Запускаем приложение
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
