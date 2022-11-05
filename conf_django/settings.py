import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# TODO mudar key como variavel de ambiente
SECRET_KEY = 'django-insecure-*&$e+al!$_$v4p(^gyep4+8_(rv8sf))a+7k=^r&4-o&hgc2g%'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'twitter',

    'rest_framework',

    'corsheaders',
]

CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = 'twitter.TwitterUser'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf_django.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd95lgbpft97ubk',
        'USER': 'mrjkbwfwfzkztu',
        'PASSWORD': 'f8a164ed97a3c0d51c1be8f37591350c8efe4699af9fdac7720c150467932f90',
        'HOST': 'ec2-107-22-122-106.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-br'


TIME_ZONE = 'America/Sao_Paulo'


USE_I18N = True


USE_L10N = True


USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "b2_twitter", "staticfiles")
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "b2_twitter", "media")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
