from django.contrib import admin
from store.models.product import Product
from store.models.comment import Comment
from store.models.category import Category


admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
