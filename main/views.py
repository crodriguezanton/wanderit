from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from datetime import datetime

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
            start_date=datetime.today()).order_by('start_date')

        return context

    def get_queryset(self):
        return self.model.objects.filter(searchrequest__userrequestmatch__wiuser__user=self.request.user).exclude(
            searchreport=None).order_by('last_search_report__min_price')


class ComingSoonView(CreateView):
    template_name = 'coming_soon.html'
    form_class = BetaForm
    success_url = '/'
