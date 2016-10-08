from django.contrib import admin
from models import *


class ReportUpdateAdmin(admin.ModelAdmin):
    list_display = ('min_price', 'abs_diff',
                    'abs_deriv', 'has_min_extremum',
                    'has_positive_change_of_concavity',
                    'has_negative_change_of_concavity',
                    'search_created')
    list_filter = ('search_report__report',)

    def min_price(self, obj):
        return obj.search_report.min_price

    def search_created(self, obj):
        return obj.search_report.flight_search.created

admin.site.register(Report)
admin.site.register(SearchReport)
admin.site.register(ReportUpdate, ReportUpdateAdmin)