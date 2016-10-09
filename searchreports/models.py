from __future__ import unicode_literals

from django.db import models
from django.db.models import Min, Avg
from django_extensions.db.models import TimeStampedModel

from skyscannerSDK.models import FlightSearch, Itinerary, Place


class Report(models.Model):
    origin = models.ForeignKey(Place, related_name='origin_city')
    destination = models.ForeignKey(Place, related_name='destination_city')
    outbound = models.DateField()
    inbound = models.DateField()

    def __unicode__(self):
        return self.origin.code + '-' + self.destination.code

    @classmethod
    def get_report(cls, flight_search):
        return cls.objects.get_or_create(
            origin=flight_search.get_origin_city(),
            destination=flight_search.get_destination_city(),
            outbound=flight_search.outbound,
            inbound=flight_search.inbound
        )[0]

    def get_carrier(self):
        return self.searchreport_set.all().order_by('-flight_search__created').first().min_price_itinerary.outbound_leg.carriers.all().first()

    def get_pricing_option(self):
        return self.searchreport_set.all().order_by('-flight_search__created').first().min_price_itinerary.pricingoption_set.all().order_by('price').first()

    def get_price_trend(self):
        dummyreports = self.searchreport_set.all().order_by('-flight_search__created').values_list('pk', flat=True)
        reports = SearchReport.objects.filter(pk__in=dummyreports)
        if reports.filter(reportupdate__has_negative_change_of_concavity=True).count():
            return 'UP'
        if reports.filter(reportupdate__has_min_extremum=True).count():
            return 'DOWN'
        return 'STABLE'

    def get_reccomendation(self):
        if self.get_price_trend() == 'UP':
            return 'WAIT'
        elif self.get_price_trend() == 'DOWN':
            return 'BUYWAIT'
        else:
            return 'BUY'

    def get_price_trend_html(self):
        if self.get_price_trend() == 'UP':
            return '<div class="red-600"><i class="icon md-trending-up"></i> Up</div>'
        elif self.get_price_trend() == 'DOWN':
            return '<div class="green-600"><i class="icon md-trending-down"></i> Down</div>'
        else:
            return '<div class=""><i class="icon md-trending-flat"></i> Stable</div>'

    def get_recommendation_html(self):
        if self.get_reccomendation() == 'WAIT':
            return '<div class="">Wait</div>'
        elif self.get_reccomendation() == 'BUYWAIT':
            return '<div class="blue-600">Buy/Wait</div>'
        else:
            return '<div class="green-600">Buy</div>'



class SearchReport(models.Model):
    flight_search = models.ForeignKey(FlightSearch)
    report = models.ForeignKey(Report)
    min_price_itinerary = models.ForeignKey(Itinerary, related_name='min_price_itinerary')
    min_price = models.FloatField()
    max_price_itinerary = models.ForeignKey(Itinerary, related_name='max_price_itinerary')
    max_price = models.FloatField()
    mean_price = models.FloatField()

    @staticmethod
    def generate(flight_search):
        min_price_itinerary = flight_search.get_min_price()
        max_price_itinerary = flight_search.get_max_price()

        search_report = SearchReport.objects.create(
            flight_search=flight_search,
            report=Report.get_report(flight_search),
            min_price_itinerary=min_price_itinerary,
            min_price=min_price_itinerary.min_price,
            max_price_itinerary=max_price_itinerary,
            max_price=max_price_itinerary.min_price,
            mean_price=flight_search.get_mean_price()
        )

        ReportUpdate.generate(search_report)

        return search_report



    def get_previous(self):
        return self.report.searchreport_set.filter(
            flight_search__created__lt=self.flight_search.created).order_by('-flight_search__created').first()

    def get_next(self):
        return self.report.searchreport_set.filter(
            flight_search__created__gt=self.flight_search.created).order_by('flight_search__created').first()


class ReportUpdate(TimeStampedModel):
    search_report = models.OneToOneField(SearchReport)
    abs_diff = models.FloatField(default=0)
    rel_diff = models.FloatField(default=0)
    abs_deriv = models.FloatField(default=0)
    rel_deriv = models.FloatField(default=0)
    has_min_extremum = models.BooleanField(default=False)
    has_positive_change_of_concavity = models.BooleanField(default=False)
    has_negative_change_of_concavity = models.BooleanField(default=False)
    first = models.BooleanField(default=False)
    prev_first = models.BooleanField(default=False)
    last = models.BooleanField(default=False)

    @classmethod
    def generate(cls, search_report):
        first = False
        prev_first = False
        last = True
        previous_sr = search_report.get_previous()
        previous = None

        if previous_sr is not None:
            previous = previous_sr.reportupdate

        if previous_sr is None:
            first = True
        elif previous_sr.get_previous() is None:
            prev_first = True

        reportupdate = cls.objects.create(
            search_report=search_report,
            first=first,
            prev_first=prev_first,
            last=last
        )

        reportupdate.update_fields(previous=previous)

        if not first:
            previous.last = False
            previous.save()

            if not prev_first and not previous.prev_first:
                previous.update_fields(previous=previous_sr.get_previous().reportupdate,
                                       next=reportupdate,
                                       prev_previous=previous_sr.get_previous().get_previous().reportupdate)

        return reportupdate

    def update_fields(self, previous=None, next=None, prev_previous=None):
        if not self.first:
            self.abs_diff = self._abs_diff(previous)
            self.rel_diff = self._rel_diff(previous)

            if not self.last:
                self.abs_deriv = self._abs_2deriv(previous, next)
                self.rel_deriv = self._rel_2deriv(previous, next)
                self.has_min_extremum = self._has_min_extremum(previous, next)

                if not self.prev_first:
                    self.has_positive_change_of_concavity = self._has_positive_change_of_concavity(prev_previous,
                                                                                                   previous, next)
                    self.has_negative_change_of_concavity = self._has_negative_change_of_concavity(prev_previous,
                                                                                                   previous, next)

        self.save()

    def _abs_diff(self, prev):
        assert prev is not None
        return self.search_report.min_price - prev.search_report.min_price

    def _rel_diff(self, prev):
        return self._abs_diff(prev) / prev.search_report.min_price

    def _abs_2deriv(self, prev, next):
        assert prev is not None
        assert next is not None
        return next._abs_diff(self) - self._abs_diff(prev)

    def _rel_2deriv(self, prev, next):
        assert prev is not None
        assert next is not None
        timedif = self.search_report.flight_search.created - prev.search_report.flight_search.created
        return (next._rel_diff(self) - self._rel_diff(prev)) / (timedif.seconds * 3600 + 1)

    def _has_min_extremum(self, prev, next):
        assert prev is not None
        assert next is not None
        return self._abs_diff(prev) <= 0 and next._abs_diff(self) > 0

    def _has_positive_change_of_concavity(self, prev_prev, prev, next):
        assert prev_prev is not None
        assert prev is not None
        assert next is not None
        return prev._abs_2deriv(prev_prev, self) <= 0 and self._abs_2deriv(prev, next) > 0

    def _has_negative_change_of_concavity(self, prev_prev, prev, next):
        assert prev_prev is not None
        assert prev is not None
        assert next is not None
        return prev._abs_2deriv(prev_prev, self) >= 0 and self._abs_2deriv(prev, next) < 0
