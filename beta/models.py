import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class BetaCode(TimeStampedModel):
    code = models.UUIDField(default=uuid.uuid4, primary_key=True)


class BetaRequest(TimeStampedModel):
    email = models.EmailField()