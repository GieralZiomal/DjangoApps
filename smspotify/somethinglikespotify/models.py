from email.policy import default
from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models

# Create your models here.

class Musicid(models.Model):
    title = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="")
    musicfile = models.FileField(default="")
