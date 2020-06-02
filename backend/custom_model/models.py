from django.conf import settings
from django.db import models


class CustomModel(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    surname = models.CharField(max_length=256,)
    verified = models.BooleanField()


# Create your models here.
