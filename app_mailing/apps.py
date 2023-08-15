from django.apps import AppConfig


class AppMailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_mailing'

    def ready(self):
        from app_mailing import scheduler
        scheduler.start()
