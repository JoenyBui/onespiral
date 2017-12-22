"""
Local Settings for django application.

"""
from .base import *


ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '*')]

# INSTALLED_APPS += ('debug_toolbar',)

# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
    'localhost',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_CREDENTIALS = True