from decouple import config


ALLOWED_HOSTS = ['bestclass-bff.fun']

CORS_ALLOWED_ORIGINS = [
    '...'
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

SECURE_TRUSTED_ORIGINS = ['...']

SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME_DB'),
        'USER': config('USER_DB'),
        'PASSWORD': config('PASSWORD_DB'),
        'HOST': config('HOST_DB'),
        'PORT': config('PORT_DB'),
    }
}
