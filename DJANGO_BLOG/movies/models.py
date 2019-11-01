from django.db import models

# Create your models here.
class Movie(models.Model) :
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=30)
    watch_grade = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.CharField(max_length=100)
    description = models.TextField()