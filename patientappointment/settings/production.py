'''
Production settings
- Set secret key from environment variable
'''

from .common import *


# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['*']

import dj_database_url
DATABASES['default'] = dj_database_url.config()


# Address of RedisToGo instance
BROKER_URL = os.environ.get('REDISTOGO_URL')