from django.db import models

class ToDo(models.Model):
 text = models.CharField(max_length=100)
 created_at = models.DateField(auto_now_add=True)
 is_closed = models.BooleanField(default=False)
 is_favourite = models.BooleanField(default=False)

class Book(models.Model):
  title = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  year = models.DateField(auto_created=True)
published_at = models.DateField(auto_now_add=True)
