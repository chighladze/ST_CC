from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'hasdfhifdo-insecure-uvfx%)@kjh4h4h5njsnfllkgbagb*f*vg^pjfz4x1h-pkfn'

DEBUG = False

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'st_callcenter_db',
        'USER': 'giorgi',
        'PASSWORD': 'q1w2Giorgi',
        'HOST': '198.18.18.109',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
