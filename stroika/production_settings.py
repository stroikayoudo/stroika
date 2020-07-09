import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'MPETs2E7r9xox6ivgo4WlTwY7gAjAeQa9GVVwXL2HOVX98t4QngXZXvDhjm67yZG'

DEBUG = False
ALLOWED_HOSTS = ['185.116.194.128']




STATIC_ROOT = os.path.join(BASE_DIR, 'static')
