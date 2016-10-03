from django.core.management.base import BaseCommand

from cron.models import FlightSearchCronJob

class Command(BaseCommand):
    help = 'Runs CronJobs'

    def handle(self, *args, **options):
        jobs = FlightSearchCronJob.objects.all()

        for job in jobs:

            self.stdout.write(self.style.WARNING('Job Strarted'))

            log = job.run()

            if log.success:
                self.stdout.write(self.style.SUCCESS('Job Ended'))
            else:
                self.stdout.write(self.style.ERROR(log.message))

        self.stdout.write(self.style.SUCCESS('All jobs ended'))