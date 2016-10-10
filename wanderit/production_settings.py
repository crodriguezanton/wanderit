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
