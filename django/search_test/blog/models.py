from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.IntegerField()
