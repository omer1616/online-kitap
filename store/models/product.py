from django.db  import models
from store.models.category import  Category
from django.utils.text import slugify
import itertools


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_stock=True)



class Product(models.Model):
    name =  models.CharField(max_length=150)
    slug = models.SlugField(max_length=40, editable=False, unique=True, null=True)
    title = models.TextField(max_length=150)
    image =  models.ImageField(upload_to="", verbose_name="Book Image", blank=True, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(to=Category, blank=True, null=True,  on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
    created_date = models.DateField()
    is_stock = models.BooleanField(verbose_name="Stok", default=True)
    objects = models.Manager()    
    products = ProductManager()


    def __str__(self) -> str:
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug =  slugify(self.name)
            
            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug=self.slug):
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)   

        super(Product, self).save(*args, **kwargs) # Call the real save() method
       
