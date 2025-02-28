import os
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()



# Access environment variables
GOOGLE_CREDS_PATH = os.getenv('GOOGLE_CREDS_PATH')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# Ensure GOOGLE_REDIRECT_URIS is loaded correctly
GOOGLE_REDIRECT_URIS = os.getenv('GOOGLE_REDIRECT_URIS')

# Check if GOOGLE_REDIRECT_URIS is loaded and split the values correctly
if GOOGLE_REDIRECT_URIS:
    GOOGLE_REDIRECT_URIS = GOOGLE_REDIRECT_URIS.split(',')
else:
    raise ValueError("GOOGLE_REDIRECT_URIS environment variable is not set or is empty")

# Ensure GOOGLE_JAVASCRIPT_ORIGINS is loaded correctly
GOOGLE_JAVASCRIPT_ORIGINS = os.getenv('GOOGLE_JAVASCRIPT_ORIGINS').split(',')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY="django-insecure-v-oe%ao*$0v7h5y))wco(akt4bdjq-a)dsw8#kocc60k1!6^s*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "api",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
    "https://sheetapp.onrender.com",
]

ROOT_URLCONF = "spreadsheet_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "spreadsheet_backend.wsgi.application"

# Fetch the DATABASE_URL from environment variables (it should be set in your environment)
database_url = 'postgresql://kamaleshdb_owner:npg_brpjJ9Gf6Wdz@ep-snowy-cake-a5ga0y37-pooler.us-east-2.aws.neon.tech/kamaleshdb'

if database_url:
    # Parse the DATABASE_URL
    url = urlparse(database_url)

    # Update the DATABASES configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:],  # Extract database name (remove leading slash)
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port or 5432,  # Default PostgreSQL port
        }
    }
else:
    raise ValueError("DATABASE_URL environment variable is not set")

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
