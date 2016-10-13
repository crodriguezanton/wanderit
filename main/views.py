from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from searchreports.models import Report


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'main/home.html'
    model = Report

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)

        context['destinations'] = self.request.user.wanderituser.userdestinationrequest_set.all()
        context['dates'] = self.request.user.wanderituser.userdatesrequest_set.all()

        return context

    def get_queryset(self):
        return self.model.objects.filter(searchrequest__userrequestmatch__wiuser__user=self.request.user).exclude(searchreport=None)