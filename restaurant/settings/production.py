from .base import *

DEBUG = False

try:
    from .base import *
except ImportError:
    pass


# STATIC FILES SETTINGS
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
