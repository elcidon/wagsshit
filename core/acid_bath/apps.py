from django.apps import AppConfig


class AcidBathConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.acid_bath'

    def ready(self):
        import apps.acid_bath.signals
