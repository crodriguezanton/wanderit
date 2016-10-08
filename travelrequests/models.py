from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

from main.models import WanderitUser
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


class UserRequestMatch(models.Model):
    destination_request = models.ForeignKey(UserDestinationRequest)
    dates_request = models.ForeignKey(UserDatesRequest)