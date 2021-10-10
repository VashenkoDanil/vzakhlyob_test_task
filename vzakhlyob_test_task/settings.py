import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv(), verbose=False, override=True)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'DEFAULT_SECRET_KEY')

DEBUG = bool(os.getenv('DEBUG', False))

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',

    'apps.account',
    'apps.api',
    'apps.story',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vzakhlyob_test_task.urls'

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

WSGI_APPLICATION = 'vzakhlyob_test_task.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DATABASES_NAME', 'db.sqlite3'),
        'USER': os.getenv('DATABASES_USER'),
        'PASSWORD': os.getenv('DATABASES_PASSWORD'),
        'HOST': os.getenv('DATABASES_HOST', 'localhost'),
        'PORT': os.getenv('DATABASES_PORT'),
    }
}


AUTH_USER_MODEL = 'account.User'


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


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PIXABAY_URL = os.getenv('PIXABAY_URL')
PIXABAY_KEY = os.getenv('PIXABAY_KEY')