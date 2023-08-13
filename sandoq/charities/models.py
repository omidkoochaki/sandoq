from django.db import models
from django.contrib.auth.models import AbstractUser


class Charity(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=11)


class User(AbstractUser):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)

