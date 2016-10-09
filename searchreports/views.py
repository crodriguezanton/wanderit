from django.views.generic import DetailView

from searchreports.models import Report, SearchReport


class ReportDetailView(DetailView):
    model = Report


class SearchReportDetailView(DetailView):
    model = SearchReport
