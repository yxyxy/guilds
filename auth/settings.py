INSTALLED_APPS = [
    ...,
    'rest_framework',  # Для API
    'rest_framework_simplejwt',  # Для JWT
    'users',  # Приложение пользователей
]

# Настройка REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Настройка базы данных (для dev)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'guilds',
        'USER': 'guilds',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Настройка для JWT
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

AUTH_USER_MODEL = 'users.CustomUser' # Добавим модель пользователя
