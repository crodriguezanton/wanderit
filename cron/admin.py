from django.contrib import admin

from cron.models import FlightSearchCronJob, CronJobLog

admin.site.register(FlightSearchCronJob)
admin.site.register(CronJobLog)
