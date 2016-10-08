from searchreports.models import SearchReport


def create_reports(queryset):

    queryset = queryset.order_by('created')

    for flight_search in queryset:

        SearchReport.generate(flight_search)