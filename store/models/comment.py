from django.db import models
from store.models.book import Book
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comments')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=500)
    evaluation = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)],
    )

