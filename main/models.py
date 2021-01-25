from django.db import models

class ToDo(models.Model):
 text = models.CharField(max_length=100)
 created_at = models.DateField(auto_now_add=True)
 is_closed = models.BooleanField(default=False)
 is_favourite = models.BooleanField(default=False)

class Book(models.Model):
  title = models.CharField(max_length=100, default= "some string")
  subtitle = models.CharField(max_length=100,  default= "some string")
  description = models.TextField(default= "some string")
  price = models.IntegerField(default=170)
  genre = models.CharField(max_length=100,  default= "some string")
  author = models.CharField(max_length=150,  default= "some string")
  year = models.DateField()
  published_at = models.DateField(auto_now_add=True, default= 170)
