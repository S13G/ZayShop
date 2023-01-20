from django.db import models

from common.models import TimeStampedUUID


# Create your models here.


class Newsletter(TimeStampedUUID):
    email = models.EmailField(max_length=300, null=True, unique=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.email}"
