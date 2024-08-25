from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
from django.conf import settings

class FirebaseTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firebase_test'

    def ready(self):
        # Initialize Firebase app only if it has not been initialized already
        if not firebase_admin._apps:
            cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIALS)
            firebase_admin.initialize_app(cred)
