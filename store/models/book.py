from django.db  import models
from store.models.category import  SubCategory



class Book(models.Model):
    name =  models.CharField(max_length=150)
    title = models.TextField(max_length=150)
    test = models.TextField(max_length=150, default=None)
    author = models.ManyToManyField(to='store.Author', related_name="authors")
    price = models.IntegerField()
    category = models.ForeignKey(to=SubCategory, blank=True, null=True,  on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
    created_date = models.DateField()
    is_stock = models.BooleanField()
    

    def __str__(self) -> str:
        return self.name

