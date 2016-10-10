from django.db import models
from django_extensions.db.models import TimeStampedModel

from cron.models import FlightSearchCronJob
from main.models import WanderitUser
from searchreports.models import Report
from skyscannerSDK.models import Place


class UserDestinationRequest(TimeStampedModel):
    wiuser = models.ForeignKey(WanderitUser)
    destination = models.ForeignKey(Place)
    max_price = models.FloatField(null=True, blank=True)


class UserDatesRequest(TimeStampedModel):
    wiuser = models.ForeignKey(WanderitUser)
    start_date = models.DateField()
    end_date = models.DateField()
    min_nights = models.IntegerField()
    max_nights = models.IntegerField()


class SearchRequest(models.Model):
    origin = models.ForeignKey(Place, related_name='origin_city_request')
    destination = models.ForeignKey(Place, related_name='destination_city_request')
    outbound = models.DateField()
    inbound = models.DateField()
    report = models.OneToOneField(Report, null=True)
    cron = models.OneToOneField(FlightSearchCronJob)


class UserRequestMatch(models.Model):
    wiuser = models.ForeignKey(WanderitUser, null=True)
    destination_request = models.ForeignKey(UserDestinationRequest)
    dates_request = models.ForeignKey(UserDatesRequest)
    search_request = models.ForeignKey(SearchRequest, null=True)