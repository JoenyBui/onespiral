from django.conf import settings

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(settings.FIREBASE_KEY)

# If used locally, then this pass in the credential.
fb_app = firebase_admin.initialize_app(cred)

# In Google App Engine, there is autodiscovery.
# firebase_admin.initialize_app()
