from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base class model with self updating created and modified fields
    """
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True