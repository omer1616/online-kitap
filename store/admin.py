from django.contrib import admin
from store.models.book  import Book
from store.models.author import Author
from store.models.comment import Comment
from store.models.category import Category, SubCategory


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(SubCategory)