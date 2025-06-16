import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2w8*b5ij0)&a4i+1ru9z58dd1g+v_4#)gs^ppz4@eb)jh3=01!'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ========== INSTALLED APPS ========== #
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # your Django app
    'rest_framework',
    'corsheaders',
]

# ========== MIDDLEWARE ========== #
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # moved up
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========== CORS CONFIG ========== #
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)

# ========== URL + WSGI ========== #
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

# ========== DATABASE ========== #
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========== PASSWORDS ========== #
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

# ========== TIME + LANGUAGE ========== #
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ========== STATIC FILES (CSS, JS, IMAGES) ========== #
STATIC_URL = '/assets/'  # 👈 matches Vite asset path

STATICFILES_DIRS = [
    BASE_DIR / 'app' / 'static',  # your Django app static
    
    BASE_DIR / 'frontend' / 'dist' / 'assets',  # ✅ Vite assets
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Used by collectstatic

# ========== MEDIA FILES ========== #
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========== TEMPLATES (REACT index.html + Django) ========== #
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend' / 'dist'],  # ✅ Vite's index.html
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========== PRIMARY KEY CONFIG ========== #
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========== RAZORPAY (if used) ========== #
RAZORPAY_KEY_ID = 'rzp_test_pr99iascS1WRtU'
RAZORPAY_KEY_SECRET = 'UTDIzPGwICnAssu3Q3lk7zUi'
