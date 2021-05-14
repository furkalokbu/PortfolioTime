# -*- coding: utf-8 -*-

import os
import datetime
gettext = lambda s: s
PROJ_MODULE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.normpath(os.path.join(PROJ_MODULE_ROOT, ".."))
root_path = lambda *args: os.path.join(ROOT, *args)
path = lambda *args: os.path.join(PROJ_MODULE_ROOT, *args)


SECRET_KEY = 'django-insecure-f2qpd#g#3ttwenflk9r_26&rrty!+wn3$-7yg=21mv!1%q3bd9'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = "portfolio.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = root_path('static')
MEDIA_URL = '/media/'
MEDIA_ROOT = root_path('media')


STATICFILES_DIRS = (
    path('static'),
)

LOCALE_PATHS = (
    path('locale'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SITE_ID = 1

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT, 'portfolio', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "users",
    "projects",
]


LOGIN_URL = "accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"




DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django User Model
AUTH_USER_MODEL = "users.CustomUser"

# django-crispy-rorms
CRISPY_TEMPLATE_PACK = "bootstrap4"

# django.contib.sites
SITE_ID = 1

# django-allauth
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True


# Django-REST-framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
}

