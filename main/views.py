from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView, CreateView, TemplateView
from datetime import datetime

from skyscannerSDK.models import Place

from beta.form import BetaForm

from searchreports.models import Report


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'main/home.html'
    model = Report

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['destinations'] = self.request.user.wanderituser.userdestinationrequest_set.all().order_by(
            'destination__name')
        context['dates'] = self.request.user.wanderituser.userdatesrequest_set.filter(
            start_date__gt=datetime.today()).order_by('start_date')

        return context

    def get_queryset(self):
        return self.model.objects.filter(searchrequest__userrequestmatch__wiuser__user=self.request.user).exclude(
            searchreport=None).order_by('last_search_report__min_price')


class ComingSoonView(CreateView):
    template_name = 'coming_soon.html'
    form_class = BetaForm
    success_url = '/'


class LandingView(TemplateView):
    template_name = 'main/landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        top_cities = Place.objects.filter(type__name='City').annotate(Count('userdestinationrequest')).order_by('-userdestinationrequest__count')

        context['top_cities'] = top_cities[:3]
        context['featured'] = top_cities[3:6]

        return context