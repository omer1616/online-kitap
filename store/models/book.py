from django.db  import models
from store.models.category import  SubCategory
from django.utils.text import slugify
import itertools


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(is_stock=True)



class Book(models.Model):
    name =  models.CharField(max_length=150)
    slug = models.SlugField(max_length=40, editable=False, unique=True, null=True)
    title = models.TextField(max_length=150)
    image =  models.ImageField(upload_to="", verbose_name="Book Image", blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(to='store.Author', related_name="authors")
    price = models.IntegerField()
    category = models.ForeignKey(to=SubCategory, blank=True, null=True,  on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
    created_date = models.DateField()
    is_stock = models.BooleanField(verbose_name="Stok", default=True)
    objects = models.Manager()    
    books = BookManager()


    def __str__(self) -> str:
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug =  slugify(self.name)
            
            for slug_id in itertools.count(1):
                if not Book.objects.filter(slug=self.slug):
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)   

        super(Book, self).save(*args, **kwargs) # Call the real save() method
       
