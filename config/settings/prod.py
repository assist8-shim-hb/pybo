from .base import *

ALLOWED_HOSTS = ['43.200.2.187']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '!74jHF6(3.y=Xm.i_VQyK}oGA4.7Mh.Z',
        'HOST': 'ls-3106bb328ade826f65facd499f5a578bdb1df6d6.cnsl2tipetzp.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
