from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=40)

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40)
