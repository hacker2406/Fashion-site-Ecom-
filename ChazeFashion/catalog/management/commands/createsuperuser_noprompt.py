from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser without prompt'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))