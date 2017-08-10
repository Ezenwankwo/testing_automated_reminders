'''
Production settings
- Set secret key from environment variable
'''

from .common import *


# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['*']

#import dj_database_url
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)


# Address of RedisToGo instance
BROKER_URL = 'redis://redistogo:c036eb72be7ea981f638be44d0d72302@angelfish.redistogo.com:11496/'