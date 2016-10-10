from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from searchreports.models import Report


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'main/home.html'
    model = Report

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)

        return context
