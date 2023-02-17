from django.db import models

from common.models import BaseModel


# Create your models here.


class Newsletter(BaseModel):
    email = models.EmailField(max_length=300, null=True, unique=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.email}"


class Contact(BaseModel):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=300, null=True, unique=True)
    subject = models.CharField(max_length=500, null=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} = {self.message}"