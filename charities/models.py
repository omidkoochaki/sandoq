from django.db import models
from django.contrib.auth.models import AbstractUser


class Charity(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=11)


class User(AbstractUser):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)


class BankAccount(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.PROTECT)
    bank = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    balance = models.PositiveIntegerField(default=0)
    last_calculation = models.DateTimeField()



