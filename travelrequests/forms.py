from django.forms import ModelForm

from skyscannerSDK.models import Place
from travelrequests.models import UserDestinationRequest


class UserDestinationRequestForm(ModelForm):
    class Meta:
        model = UserDestinationRequest
        fields = ('destination',)

    def __init__(self, *args, **kwargs):
        super(UserDestinationRequestForm, self).__init__(*args, **kwargs)
        self.fields['destination'].queryset = Place.objects.filter(type__name='City')
