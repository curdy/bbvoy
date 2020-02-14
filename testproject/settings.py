import os

DEBUG = True

BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTH_PASSWORD_VALIDATORS = [{"NAME": "testapp.validators.Is666"}]

SECRET_KEY = "_"

MIDDLEWARE = [  'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',]


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "templated_mail",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "social_django",
    "testapp",

    'django.contrib.admin',
    
    'landing',
    'dashboard',
)

STATIC_URL = "/static/"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
}

ROOT_URLCONF = "urls"

#TEMPLATES = [
#    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
#]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'libs', 'templates')],
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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "djoser.social.backends.facebook.FacebookOAuth2Override",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.steam.SteamOpenId",
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("FACEBOOK_KEY", "")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("FACEBOOK_SECRET", "")

SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "id, name, email"}

SOCIAL_AUTH_STEAM_API_KEY = os.environ.get("STEAM_API_KEY", "")
SOCIAL_AUTH_OPENID_TRUST_ROOT = "http://127.0.0.1:8000/"

DJOSER = {
    "SEND_ACTIVATION_EMAIL": False,
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://127.0.0.1:8000/"],
}

JWT_AUTH = {"JWT_ALLOW_REFRESH": True}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "libs", "static"),
]


#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'bbvoytest@gmail.com'
SERVER_EMAIL = 'bbvoytest@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bbvoytest@gmail.com'
EMAIL_HOST_PASSWORD = 'Mathase$123'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
