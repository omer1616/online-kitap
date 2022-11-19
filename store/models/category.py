from django.db import models
from django.utils.text import slugify
import itertools

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=40)

    def __str__(self) -> str:
        return self.name



    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            
            for slug_id in itertools.count(1):
                if not Category.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id) 

        super(Category, self).save(*args, **kwargs) # Call the real save() method   