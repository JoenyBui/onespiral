from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '*.wespiral.com')]

# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    '*.wespiral.com'
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

APPEND_SLASH = True

FIREBASE_KEY = os.path.join(BASE_DIR, '../secrets', 'fb-prod-key.json')

# TODO: Remove email backend for now because it doesn't quite work.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
