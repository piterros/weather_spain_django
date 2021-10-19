from django.core.management.base import BaseCommand
from django.utils import timezone
from get_stats.database import add_to_database




class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        add_to_database()