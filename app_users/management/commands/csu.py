from django.core.management import BaseCommand
from app_users.models import User
from django.conf import settings


class Command(BaseCommand):
    """Executable commands in cmd with manage.py."""
    def handle(self, *args, **options):
        """Create superuser with custom attributes."""
        user = User.objects.create(
            email=settings.SUPERUSER_EMAIL,
            first_name=settings.SUPERUSER_FIRST_NAME,
            last_name=settings.SUPERUSER_LAST_NAME,
            surname=settings.SUPERUSER_SURNAME,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(settings.SUPERUSER_PASSWORD)
        user.save()
