"""
Common Django settings for the appointments project.
See the local, test, and production settings modules for the values used
in each environment.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nx7e9w_nq@qbr&jec$5vgm^$z$dl2f*&i(k(e*w4^r9i3lyci6'

# Most important settings

#Twilio API
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')


# Address of Redis instance, our Celery broker
#BROKER_URL = 'redis://localhost:6379/0'
BROKER_POOL_LIMIT = 8

# Reminder time: how early text messages are sent in advance of appointments
REMINDER_TIME = 30 # minutes

ALLOWED_HOSTS = ['*']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

THIRD_PARTY_APPS = (
    'bootstrap3',
    'django_forms_bootstrap',
    'timezone_field'
)

LOCAL_APPS = (
    'appointmentmanager',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'patientappointment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
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


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
    #'default': {
       # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
       # 'NAME': 'patientappointment',
       # 'USER': 'exalted',
       # 'PASSWORD': 'charity24',
       # 'HOST': '127.0.0.1',
       # 'PORT': '5432',
   # }
#}

import dj_database_url 
DATABASES = {'default': dj_database_url.parse('postgres://jqtpelyhqjpccl:b210014b8a52852403e0047040d4e665c6d28401ac83ec7a6afcc9d2ff941dbc@ec2-107-20-186-238.compute-1.amazonaws.com:5432/dafs3oulj27jf7')}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = BASE_DIR + '/staticfiles'

STATIC_URL = '/static/'


