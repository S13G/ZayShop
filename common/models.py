from uuid import uuid4

from django.db import models


# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
