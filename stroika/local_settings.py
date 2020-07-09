import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'hello'

DEBUG = True
ALLOWED_HOSTS = []
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
# EMAIL_BACKEND = (
#     'django.core.mail.backends.console.EmailBackend'
# )
