from django.core.management.base import BaseCommand
from memos.tasks import send_daily_summaries

class Command(BaseCommand):
    help = "Send daily voice memo summaries"

    def handle(self, *args, **kwargs):
        send_daily_summaries()
        self.stdout.write(self.style.SUCCESS("Daily summaries sent"))