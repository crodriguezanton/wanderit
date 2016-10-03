from wanderit.settings import *


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '130.211.87.224',
        'NAME': 'wanderit',
        'USER': 'root',
        'PASSWORD': 'beatbcn4113',
    }
}