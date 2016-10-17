from wanderit.common_settings import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'mydb',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '130.211.87.224',
            'NAME': 'wanderit',
            'USER': 'root',
            'PASSWORD': 'beatbcn4113',
        }
    }


""" Static files and media (CSS, JavaScript, Images) """
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, '../static_server/media/')
STATIC_ROOT = os.path.join(ENV_PATH, '../static_server/static/')

# This one is just useful during development, on production statics and media should be served by nginx / apache
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

RAVEN_CONFIG = {
    'dsn': 'https://9cf7753c476b4127b02d337e78781a86:95efbc9a16354e5e863e7c2b43ebcc50@sentry.io/106800',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}