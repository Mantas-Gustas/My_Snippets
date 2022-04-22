"""
Django settings for dataflair project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from os import *
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#p$usud!ak=sxf7d5f7n$dia$q)mabwcj0dg31)og-_j&78nwo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'student.apps.StudentConfig',
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
    
    #DataFlair #Caching Middleware
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dataflair.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['student.templates'],
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

WSGI_APPLICATION = 'dataflair.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # new database program mysql
        'NAME': '',  # NEED TO ENTER HERE the name of the database in the phphomepage Xampp
        'USER': 'root',
        'PASSWORD': '',  # keep this field empty as filling it can produce errors for some users
        'HOST': '',  # this is HOST server, by leaving it blank it defaults to localhost
        'PORT': '',
        'OPTIONS': { 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}  # in this, we are actually passing the SQL as a string through Python which then the SQL server parses itself - It is essentially SQL, being passed on as a string.
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#DataFlair #Database Cache
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'dataflair_cachetable',
        #  below you cna write OPTIONS
    }
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # this is where you need to create your ENVIRON Variable
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # the EMAIL_USER and EMAIL_PASS are Enviro Variables holding sensitive info
# to create enviro variables see below instructions
# 1. Install Django Environ - In your terminal, inside the project directory, type: pip install django-environ
# 2. Import environ in settings.py - import environ
# 3. Initialise environ - Below your import in settings.py:
""" import environ
# Initialise environment variables #
env = environ.Env()
environ.Env.read_env() """
# 4. Create your .env file - In the same directory as settings.py, create a file called ‘.env’
# 5. Declare your environment variables in .env - Make sure you don’t use quotations around strings.
# 6. IMPORTANT: Add your .env file to .gitignore
# 7. Replace all references to your environment variables in settings.py ‘USER’: env(‘DATABASE_USER’), or SECRET_KEY = env(‘SECRET_KEY’)