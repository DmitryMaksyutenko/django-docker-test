from django.conf import settings

settings.INSTALLED_APPS += ['silk']
settings.MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

