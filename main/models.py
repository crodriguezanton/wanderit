from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from skyscannerSDK.models import Place


class WanderitUser(models.Model):
    user = models.OneToOneField(User)
    origin = models.ForeignKey(Place, null=True)
