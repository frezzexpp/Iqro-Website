# --package and modules:
from datetime import timedelta
from pathlib import Path
import os
import environ
from django.utils.translation import gettext_lazy as _
# ________________________________________________________________________________
# ________________________________________________________________________________



# from env file
root = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env(env.str(root(), '.env'))
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Base_dir,Secret_key,Debug,Hosts_permission:
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.str('ALLOWED_HOSTS', default='').split(' ')

BASE_DIR = root()
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Application definition:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# rest_framework:
INSTALLED_APPS += [
    'rest_framework',
]

# swagger:
INSTALLED_APPS += [
    'drf_spectacular',
]

# autentifikatsiya
INSTALLED_APPS += [
    'djoser',

]


# other
INSTALLED_APPS += [
    'django_filters',
    'corsheaders',
    'phonenumber_field',
]


# apps:
INSTALLED_APPS += [
    'about',
    'api',
    'contact',
    'homepage',
    'imageproxy',
    'project',
    'users',
]
INSTALLED_APPS += ['storages']


# Custom user model
AUTH_USER_MODEL = 'users.CustomUsers'
# ________________________________________________________________________________
# ________________________________________________________________________________



# Minio sitedida rasm url korinishda olish uchun:
MINIO_STORAGE_ENDPOINT = env.str("MINIO_STORAGE_ENDPOINT", "")
MINIO_STORAGE_ACCESS_KEY = env.str("MINIO_STORAGE_ACCESS_KEY", "")
MINIO_STORAGE_SECRET_KEY = env.str("MINIO_STORAGE_SECRET_KEY", "")
MINIO_STORAGE_USE_HTTPS = env.bool("MINIO_STORAGE_USE_HTTPS", False)
MINIO_STORAGE_MEDIA_BUCKET_NAME = env.str("MINIO_STORAGE_MEDIA_BUCKET_NAME", "")
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = env.bool("MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET", False)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ENDPOINT_URL = MINIO_STORAGE_ENDPOINT
AWS_ACCESS_KEY_ID = MINIO_STORAGE_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = MINIO_STORAGE_SECRET_KEY
AWS_S3_USE_SSL = MINIO_STORAGE_USE_HTTPS
AWS_STORAGE_BUCKET_NAME = MINIO_STORAGE_MEDIA_BUCKET_NAME
AWS_QUERYSTRING_AUTH = False
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Middleware:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Templates:
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Database:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('PG_DATABASE', 'postgres'),
        'USER': env.str('PG_USER', 'postgres'),
        'PASSWORD': env.str('PG_PASSWORD', 'postgres'),
        'HOST': env.str('DB_HOST', 'localhost'),
        'PORT': env.int('DB_PORT', 5432),
    },
    'extra': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}
# ________________________________________________________________________________
# ________________________________________________________________________________



REST_FRAMEWORK = {

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 70
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ________________________________________________________________________________
# ________________________________________________________________________________



# --Lagnauges:
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = [
   ('uz', _('Uzbek')),
   ('en', _('English')),
   ('ru', _('Russian')),

]
# ________________________________________________________________________________
# ________________________________________________________________________________



# Static root:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ________________________________________________________________________________
# ________________________________________________________________________________



# Cors headers:
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CSRF_COOKIE_SECURE = False
# ________________________________________________________________________________
# ________________________________________________________________________________



#TELEGRAM SETTINGS
TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN', ''),
TELEGRAM_CHANNEL_ID = env.int('TELEGRAM_CHANNEL_ID', ''),
# ________________________________________________________________________________
# ________________________________________________________________________________



# --Swagger settings:
SPECTACULAR_SETTINGS = {
    'TITLE': 'Iqro Website',
        'DESCRIPTION': 'Official Iqro Agency Website',
    'VERSION': '1.0.0',

    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated'],

    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication'],

    'SWAGGER_UI_SETTINGS': {
        'DeepLinking': True,
        'DisplayOperationId': True,
    },

    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,
}
# ________________________________________________________________________________
# ________________________________________________________________________________



# jwt settings:
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}
# ________________________________________________________________________________
# ________________________________________________________________________________