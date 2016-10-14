from django.forms import ModelForm

from beta.models import BetaRequest


class BetaForm(ModelForm):
    class Meta:
        model = BetaRequest
        fields = ('email',)