'''
Production settings
- Set secret key from environment variable
'''

from .common import *


# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['*']

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Address of RedisToGo instance
BROKER_URL = os.environ.get('REDISTOGO_URL')