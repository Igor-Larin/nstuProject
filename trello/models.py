from django.db import models


# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=15)


class Card(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('User', models.PROTECT, null=True)


class Task(models.Model):
    text = models.CharField(max_length=200)
    timelimit = models.IntegerField()
    card = models.ForeignKey('Card', models.PROTECT, null=True)
