from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio =  models.TextField(max_length=1000)
    birth_date =  models.DateField(verbose_name="Birt Date")
