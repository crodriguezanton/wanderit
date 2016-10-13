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

    def save(self, **kwargs):
        super(UserDestinationRequest, self).save(**kwargs)
        dates_requests = UserDatesRequest.objects.filter(wiuser=self.wiuser)
        for request in dates_requests:
            UserRequestMatch.objects.get_or_create(
                wiuser = self.wiuser,
                destination_request = self,
                dates_request = request
            )


class UserDatesRequest(TimeStampedModel):
    wiuser = models.ForeignKey(WanderitUser)
    start_date = models.DateField()
    end_date = models.DateField()
    min_nights = models.IntegerField(default=0)
    max_nights = models.IntegerField(default=0)

    def save(self, **kwargs):
        super(UserDatesRequest, self).save(**kwargs)
        destination_requests = UserDestinationRequest.objects.filter(wiuser=self.wiuser)
        for request in destination_requests:
            UserRequestMatch.objects.get_or_create(
                wiuser=self.wiuser,
                destination_request=request,
                dates_request=self
            )


class SearchRequest(models.Model):
    origin = models.ForeignKey(Place, related_name='origin_city_request')
    destination = models.ForeignKey(Place, related_name='destination_city_request')
    outbound = models.DateField()
    inbound = models.DateField()
    report = models.OneToOneField(Report, null=True, blank=True)
    cron = models.OneToOneField(FlightSearchCronJob, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not hasattr(self, 'cron'):
            self.cron = FlightSearchCronJob.objects.get_or_create(
                origin = self.origin.code,
                destination = self.destination.code,
                outbound = self.outbound,
                inbound = self.inbound
            )[0]

        if not hasattr(self, 'report'):
            self.report = Report.objects.get_or_create(
                origin = self.origin,
                destination = self.destination,
                outbound=self.outbound,
                inbound=self.inbound
            )[0]

        super(SearchRequest, self).save(force_insert=force_insert, force_update=force_update, using=using,
                                           update_fields=update_fields)


class UserRequestMatch(models.Model):
    wiuser = models.ForeignKey(WanderitUser, null=True)
    destination_request = models.ForeignKey(UserDestinationRequest, on_delete=models.CASCADE)
    dates_request = models.ForeignKey(UserDatesRequest, on_delete=models.CASCADE)
    search_request = models.ForeignKey(SearchRequest, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.search_request is None:
            self.search_request = SearchRequest.objects.get_or_create(
                origin = self.destination_request.wiuser.origin,
                destination = self.destination_request.destination,
                outbound = self.dates_request.start_date,
                inbound = self.dates_request.end_date,
            )[0]

        super(UserRequestMatch, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)