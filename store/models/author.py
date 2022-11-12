from django.db  import models




class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(max_length=500)
    book = models.ManyToManyField(to='store.Book', related_name="books")
    date_of_birth = models.DateField()
    
    

