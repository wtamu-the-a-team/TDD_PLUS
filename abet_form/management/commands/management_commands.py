from django.core.management.base import BaseCommand

from abet_form.models import Application, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("WARNING: REMOVING ALL OBJECTS")
        User.objects.all().delete()
        Application.objects.all().delete()
