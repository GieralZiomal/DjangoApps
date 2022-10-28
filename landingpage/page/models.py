from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class kurs(models.Model):
    title = models.CharField(max_length=50)
    tekst1 = models.CharField(max_length=500)
    tekst2 = models.CharField(max_length=500)
    obrazek1 = models.FileField()
    obrazek2 = models.FileField(default=0)