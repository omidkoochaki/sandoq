from django.db import models

from sandoq.charities.models import Charity


class Project(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=256)
    goal_budget = models.PositiveIntegerField(default=0)


class Deposit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    fee = models.PositiveIntegerField(default=0)
    depositor = models.CharField(max_length=128)
    msg = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Withdraw(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    fee = models.PositiveIntegerField(default=0)
    withdrawer = models.CharField(max_length=128)
    reason = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)


