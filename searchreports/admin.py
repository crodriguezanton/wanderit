from django.contrib import admin
from models import *


class ReportUpdateAdmin(admin.ModelAdmin):
    fields = ('search_report__flight_search__created', 'search_report__min_price', 'abs_diff',
              'abs_deriv', 'has_min_extremum', 'has_positive_change_of_concavity', 'has_negative_change_of_concavity')
    list_filter = ('search_report__report',)

admin.site.register(Report)
admin.site.register(SearchReport)
admin.site.register(ReportUpdate, ReportUpdateAdmin)