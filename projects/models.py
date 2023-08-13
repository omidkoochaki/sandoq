from django.db import models

from charities.models import Charity, User


class Project(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=256)
    goal_budget = models.PositiveIntegerField(default=0)


class Deposit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    fee = models.PositiveIntegerField(default=0)
    depositor_name = models.CharField(max_length=128)
    Registrar = models.ForeignKey(User, on_delete=models.PROTECT)
    msg = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Withdraw(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    fee = models.PositiveIntegerField(default=0)
    withdrawer = models.ForeignKey(User, on_delete=models.PROTECT)
    reason = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)


