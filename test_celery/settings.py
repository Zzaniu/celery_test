"""
Django settings for test_celery project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from kombu import Exchange, Queue
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cg%ds*ccj6d*$yuht!&@70m8-&3g2+a_b2xeld3srx@t^usy+!'

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
    'test_1.apps.Test1Config',
    'djcelery',
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

ROOT_URLCONF = 'test_celery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'test_celery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#celery相关
import djcelery
djcelery.setup_loader()
# borker redis://:密码@ip:port/数据库
BROKER_URL = 'redis://:admin@111.230.151.179:6379/15'
BROKER_TRANSPORT = 'redis'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = ("test_1.tasks")
CELERYD_CONCURRENCY = 4  # 并发worker数
CELERY_IGNORE_RESULT = True
CELERY_DEFAULT_EXCHANGE = 'agent'
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERT_QUEUES = (
    Queue('default', exchange='agent', routing_key='default'),
    Queue('machine1', exchange='agent', routing_key='machine1'),
    Queue('machine2', exchange='agent', routing_key='machine2'),
)

# 下面是定时任务的设置
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    # #定时任务:　每天的凌晨1:00分，执行任务()
    u'大爷肆': {
        'task': 'test_1.tasks.Task4',
        'schedule': crontab(minute=30, hour=11),
        "args": ()
    },
    u'大爷伍': {
        'task': 'test_1.tasks.Task5',
        'schedule': crontab(minute=30, hour=11),
        "args": ()
    },
}
# 定时任务指定路由
CELERY_ROUTES = {
    'test_1.tasks.Task5': {'queue': 'machine2', 'routing_key': 'machine2'},
}

