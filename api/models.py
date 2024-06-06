from django.db import models
from django import forms
# Create your models here.

class Data(models.Model):
    date = models.DateField()
    drowsy = models.IntegerField()
    total = models.IntegerField()
