from django.db import models

# Create your models here.

class New(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()