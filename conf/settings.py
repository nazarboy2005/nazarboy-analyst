import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'cloudinary_storage',
    'cloudinary',
    'whitenoise',

    # My apps
    'home',
    'resume',
    'certifications',
    'projects',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Ensures static file handling
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, engine='django.db.backends.postgresql')
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media Files Configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'assets']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # ✅ Added for local fallback

# ✅ Cloudinary Configuration (Now Secure)
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    UPLOAD_PRESET='Public',
    SECURE=True,  # Forces HTTPS
    SIGN_URL=True
)


# ✅ Use Cloudinary for Media Storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ✅ Security & Debug Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
