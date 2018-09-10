DATABASES = {'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'timezone',
}}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'timezones',
]

MIDDLEWARE_CLASSES = []
#
# ROOT_URLCONF = 'app.urls'

SECRET_KEY = 'test'
