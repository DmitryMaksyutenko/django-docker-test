from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseDates(models.Model):
    
    class Meta:
        abstract = True

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class User(AbstractUser):

    date_updated = models.DateTimeField(auto_now=True)
