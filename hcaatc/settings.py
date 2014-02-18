# Django settings for hcaatc project.
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'hcaadb',                     
        'USER': 'hcau',                      
        'PASSWORD': 'HCA123',                
        'HOST': '',                      
        'PORT': '',                      
    }
}

TIME_ZONE = 'Asia/Kolkata'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True

USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
     os.path.join(os.path.dirname(__file__), 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'x+kem&m&_cb*iyb@#(7t)g1gd8709a5g-g#iq2-d=(@z)@#0u&'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hcaatc.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'hca',
    'registration',
    'django.contrib.humanize',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = " "
EMAIL_HOST_PASSWORD = " "
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'horizon.computer47@gmail.com'
ACCOUNT_ACTIVATION_DAYS = 7


