import uuid

from django.db import models
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel

from skyscannerSDK.utils import SearchErrorException, search_flights

from cron.constants import CRONJOB_TYPE_CHOICES, PRIORITY, TIME_UNITS


class CronJob(TimeStampedModel):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField(default=0, choices=CRONJOB_TYPE_CHOICES)

    priority = models.IntegerField(default=2, choices=PRIORITY)

    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    interval = models.IntegerField(default=1)
    unit = models.IntegerField(default=1, choices=TIME_UNITS)

    last_performed = models.DateTimeField(blank=True, null=True)

    def run(self):
        return CronJobLog.objects.create(cronjob=self, start=now())


class FlightSearchCronJob(CronJob):

    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    outbound = models.DateField()
    inbound = models.DateField()
    passengers = models.IntegerField(default=1)

    def run(self):

        log = super(FlightSearchCronJob, self).run()

        try:
            fs = search_flights(self.origin, self.destination, self.outbound, self.inbound, self.passengers)
            log.message = fs.__unicode__()
            log.success = True
            log.end = now()
        except SearchErrorException as e:
            print(e)
            log.message = 'Search Error: ' + e.message
            log.success = False
            log.end = now()
        except Exception as e:
            print(e)
            log.message = e.message
            log.success = False
            log.end = now()

        log.save()

        return log


class CronJobLog(models.Model):

    cronjob = models.ForeignKey(CronJob)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    success = models.BooleanField(default=True)
    message = models.TextField()


