"""
Django settings for ms4ecommerce project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from os import path
import os
import dj_database_url

if path.exists("env.py"):
    import env
    
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
# True only if in development environ
#DEBUG = 'DEVELOPMENT' in os.eviron

ALLOWED_HOSTS = ['backpocket-store.herokuapp.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django-Allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # end Django-Allauth
    'home',
    'products',
    'shopping_bag',
    'checkout',
    'profiles',
    # Django-Countries and Cities
    'django_countries',
    #'cities',
    'crispy_forms',
    'storages',
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

ROOT_URLCONF = 'ms4ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Templates directory
            os.path.join(BASE_DIR, 'templates'),
            # Allauth directory
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # Allows use {{ MEDIA_URL }} in templates
                'django.template.context_processors.media',
                'django.template.context_processors.request',  # Required by django-allauth
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                # Making the shopping bag context available for the entire project
                # folder.file.function
                'shopping_bag.context.bag_context',
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Default: Not defined
# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific sites and a single
# database can manage content for multiple sites.
SITE_ID = 1

# Allauth allowing to --->
ACCOUNT_AUTHENTICATIONMETHOD = 'username_email'  # Either username or email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGHT = 4
LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/success'
LOGIN_REDIRECT_URL = '/'


WSGI_APPLICATION = 'ms4ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES ={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
"""
    DATABASES = {
        'default': dj_database_url.parse('postgres://pspnwufjyiivfx:8f40b6edb0a89ae86ba9d7202d8e56565348e9fc97117e5931d180a52c138786@ec2-18-203-7-163.eu-west-1.compute.amazonaws.com:5432/d9hqq5acui2p40')
    }
"""

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'static/'

# Adding statics files
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)  # Tupla
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "staticfiles"), )

# Static route for amazon services - Django Collectstatic utility


# Media Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2009 20:00:00 GTM',
        'CacheControl': 'max-age=94608000',
    }
    # AWS S3 Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'backpocket-store'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}s3.amazonaws.com'

    # Static and Media Files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storage.MediaStorage'
    MEDIAFILE_LOCATION = 'media'

    # Overide static and edia URls in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Stripe's Setting
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'GBP'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_KEY = os.getenv('STRIPE_WH_KEY', '')

if 'DEVELOPMENT' in os.environ:
    # Sending  new account confimation emails to the console temporary
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'costumerservice@backpoket.com'
else:
    # Sending  new account confimation emails to the console temporary
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
