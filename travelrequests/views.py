from django.views.generic import CreateView

from travelrequests.forms import UserDestinationRequestForm
from travelrequests.models import UserDatesRequest, UserDestinationRequest


class UserDatesRequestCreateView(CreateView):
    model = UserDatesRequest
    fields = ('start_date', 'end_date')


class UserDestinationRequestCreateView(CreateView):
    model = UserDestinationRequest
    form_class = UserDestinationRequestForm