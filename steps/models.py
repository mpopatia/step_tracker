from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class StepCount(models.Model):
    owner = models.ForeignKey(User)
    steps = models.IntegerField(default=0)
    dateCreated = models.DateField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True)

    def owner_email(self):
        return self.owner.email


class Tester(models.Model):
    count = models.IntegerField(default=0)

class EmailCounter(models.Model):
    dateCreated = models.DateField()
