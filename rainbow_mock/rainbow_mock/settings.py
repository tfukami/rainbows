"""
Django settings for rainbow_mock project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from .settings_common import *
import os

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

# LOGGING setting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'schedule': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
