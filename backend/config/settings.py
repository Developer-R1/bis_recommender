"""
Django settings for the BIS Standards Recommender prototype.

Kept deliberately simple for a free-tier, single-instance hackathon deployment.
See README.md before changing anything here.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# The frontend lives as a sibling folder to backend/ (../frontend). Django
# serves it directly (see below + config/urls.py) so the whole app is ONE
# deployed service at ONE URL — a reviewer opens the link and it just works,
# no separate frontend host, no CORS, no pasting an API URL anywhere.
FRONTEND_DIR = BASE_DIR.parent / "frontend"

# --- Core -------------------------------------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-insecure-key-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "*")
ALLOWED_HOSTS = [h.strip() for h in _hosts.split(",") if h.strip()]

# --- Apps ---------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "standards",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

# --- Database -------------------------------------------------------------
# SQLite is enough for a curated, read-mostly MVP knowledge base.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("DJANGO_DB_PATH", BASE_DIR / "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = []  # not relevant: only the admin login uses auth, and that's a single trusted user

# --- i18n -------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# --- Static files ---------------------------------------------------------
# Two independent things WhiteNoise serves:
#  1. STATIC_URL/STATIC_ROOT: Django's own static files (admin CSS/JS etc.),
#     the normal Django convention.
#  2. WHITENOISE_ROOT: the frontend's assets/ folder, served at the site
#     ROOT (not prefixed), e.g. frontend/assets/css/style.css -> /assets/css/style.css.
#     This is what lets one Django deployment serve the whole app.
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
if (FRONTEND_DIR / "assets").exists():
    WHITENOISE_ROOT = str(FRONTEND_DIR)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- CORS -------------------------------------------------------------
# The frontend is hosted on a different origin (GitHub Pages / Netlify),
# so the API must accept cross-origin requests. This is a public read-mostly
# demo API with no user accounts, so allow-all is acceptable for the MVP.
# Tighten this (CORS_ALLOWED_ORIGINS = [...]) before any real deployment.
CORS_ALLOW_ALL_ORIGINS = True

# --- App-specific settings ------------------------------------------------
# Shown in every API response so a reviewer knows how fresh the curated data is.
DATA_AS_OF = os.environ.get("DATA_AS_OF", "2026-09-27")
