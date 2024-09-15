from pathlib import Path
from os import getenv, path
from django.core.management.utils import get_random_secret_key
from datetime import timedelta
import dj_database_url
import sys
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env'

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

DEVELOPMENT_MODE = getenv('DEVELOPMENT_MODE', 'False') == 'True'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS','127.0.0.1,localhost').split(',')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
  'apps.users',
  'apps.hotels',
  'apps.serviceDirectory',
  'apps.reservations'
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "djoser",
    "corsheaders",
    "storages",
    # "rest_framework_simplejwt",
    # "rest_framework_simplejwt.token_blacklist",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEVELOPMENT_MODE is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if getenv('DATABASE_URL', None) is None:
        raise Exception('DATABASE_URL environment variable not defined')
    DATABASES = {
        'default': dj_database_url.parse(getenv('DATABASE_URL')),
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
if DEVELOPMENT_MODE is True:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'static'

    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    AWS_S3_ACCESS_KEY_ID = getenv('AWS_S3_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = getenv('AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = getenv('AWS_S3_REGION_NAME')
    # empieza
    AWS_S3_ENDPOINT_URL = f'https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com'
    AWS_S3_CUSTOM_DOMAIN = getenv('AWS_S3_CUSTOM_DOMAIN')
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400'
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    AWS_MEDIA_LOCATION = 'media'
    # termina
    STORAGES = {
        'default': {'BACKEND': 'custom_storages.CustomS3Boto3Storage'},
        'staticfiles': {'BACKEND': 'storages.backends.s3boto3.S3StaticStorage'}
    }

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.UserAccount'

CORS_ALLOWED_ORIGINS = getenv('CORS_ALLOWED_ORIGINS','http://localhost:3000,http://127.0.0.1:3000').split(',')
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': getenv('SIGNING_SECRET_KEY'),
    'AUTH_HEADER_TYPES': ('JWT',)
}

# DJOSER = {
#     # CHAGNE THIS
#     "PASSWORD_RESET_CONFIRM_URL": "password-reset/{uid}/{token}",
#     "TOKEN_MODEL": None,
#     "SEND_ACTIVATION_EMAIL": False,
#     "USER_CREATE_PASSWORD_RETYPE": True,
#     "PASSWORD_RESET_CONFIRM_RETYPE": True,
# }
DJOSER = {
    'SERIALIZERS': {
        'user_create': 'apps.users.serializers.CustomUserCreateSerializer',
    },
}

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
# ]