"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hohg-a_*bzov)$517xcg21ze0&do9+&mn53*r5zh*v@y79f2qu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'project',
    'article',
    'hackathon',

    # third part apps
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'hostname.example.com'
# )


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'NAME': os.environ.get("MYSQL_DATABASE", 'dispider'),
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ.get("MYSQL_USER", 'root'),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD", ''),
        'HOST': os.environ.get("MYSQL_HOST", 'localhost'),
        'PORT': os.environ.get("MYSQL_PORT", 3306),
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Custom Settings
DOMAIN = 'api.joway.wang'
SCHEDULER_CALLBACK_API = 'http://' + DOMAIN + '/callback/'

# REDIS
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
if REDIS_PASSWORD:
    REDIS_CONN_URL = 'redis://:' + REDIS_PASSWORD + '@' + REDIS_HOST + ':' + str(REDIS_PORT)
else:
    REDIS_CONN_URL = 'redis://' + REDIS_HOST + ':' + str(REDIS_PORT)
REDIS_CELERY_BROKER_DB = 0
REDIS_CELERY_RESULT_DB = 1
REDIS_URL_DB = 2

# elastic
ELASTIC_PORT = os.environ.get('ELASTIC_PORT', '9200')
ELASTIC_HOSTS = [os.environ.get('ELASTIC_HOSTS', 'localhost') + ELASTIC_PORT]
ELASTIC_AUTH_USER = 'root'
ELASTIC_AUTH_PASSWORD = 'password'

try:
    from .local_settings import *
except ImportError:
    pass
