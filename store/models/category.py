from enum import unique
from pyexpat import model
from re import T
from statistics import mode
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db  import models


class Category(models.Model):
    name =  models.CharField(max_length=255)
    slug =  models.SlugField(max_length=255,  uniqe=True)


    class  Meta:
        verbose_name_plural = 'catagories'

    def __str__(self) -> str:
        return self.name



class SubCategory(models.Model):
    category =  models.models.ForeignKey(to=Category, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    slug =  models.SlugField(max_length=255, unique=True)


    class  Meta:
        verbose_name_plural = 'subcategories'
    def __str__(self) -> str:
        return self.name