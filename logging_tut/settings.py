"""
Django settings for logging_tut project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5f=)oejo0ya^e&c3bni&%sodgqx*4vr%p@38tiy-e&lzud*ck%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'logging_tut.urls'

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

WSGI_APPLICATION = 'logging_tut.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DataFlair #Logging Information
LOGGING = {
    'version': 1,
    # Version of logging
    'disable_existing_loggers': False,
    #disable logging 
    # Handlers #############################################################
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'dataflair-debug.log',
        },
########################################################################
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    # Loggers ####################################################################
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG')
        },
    },
}

# I know the code is a bit large but it???s very easy to grasp. We get a built-in variable LOGGING from Django. The logging???s default values come from this dictionary. Since we are configuring settings using a dictionary it???s called the dictConfig method.

# There are some important keys inside the LOGGING dictionary.

# version
# disable_existing_loggers
# handlers
# loggers
# Let???s discuss them one by one. The version key tells the schema version. It???s important that it has value. It???s by default 1.

# The next key is disable_existing_loggers. This key is to tell Django to do not disable loggers. By default, Django uses some of its own loggers. These loggers are connected with Django ORM and other inner parts of Django. This key is by default True. So, it will disable those loggers.

# There are various database queries and function calls which the loggers log. Therefore, it is recommended that you don???t True this Key.

# Handlers is the 3rd key. As we discussed, handlers handle the message and pass them to console, file, etc. The handlers itself is a dictionary. That dictionary-key names will be the names of the handlers. There are various handlers provided by the logging module. We are using two handlers here.

# 1. FileHandler: logger-name ??? filehandler

# The FileHandler will store the logs in a file. As you can see, we have given the filename as dataflair-debug.log. The level defines, until what level the logger shall commit logs.

# Note:

# Log files are generally stored with .log extension. This file can only be edited with permissions. It can only be appended.

# 2. StreamHandler: logger name ??? console

# The stream handler will stream the log on console. This is not a recommended method. There is a limit of characters until the command line shows you logs. Since logs are too big to handle by command line therefore we need file-handlers.

# There are more handlers like mailhandlers, AdminEmailHandler etc.

# The AdminEmailHandler is a great addition to the opensource module.

# Loggers are the ones that will log your server or software information. Loggers are also a dictionary type. It has a similar architecture as handlers. Although, there are different attributes and other properties.