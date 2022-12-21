from django.db import models

# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=255)
    ratings = models.FloatField()
    change = models.FloatField()

