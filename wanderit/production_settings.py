from wanderit.settings import *


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/beat-bcn:beat-bcn',
        'NAME': 'wanderit',
        'USER': 'root',
    }
}