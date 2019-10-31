from django.db import models

# Create your models here.
class Doppelganger(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()
    job = models.CharField(max_length=30)