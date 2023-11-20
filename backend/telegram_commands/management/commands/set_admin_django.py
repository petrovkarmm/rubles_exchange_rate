from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a superuser with username admin and password 123'

    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            username='admin',
            password='123',
            email='admin@admin.com'
        )

        self.stdout.write(self.style.SUCCESS('Superuser created --- \n'
                                            'login: admin, password: 123'))

