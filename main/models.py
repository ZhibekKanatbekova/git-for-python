from django.db import models

class ToDo(models.Model):
 text = models.CharField(max_length=100)
 created_at = models.DateField(auto_now=True)
 is_closed = models.BooleanField(default=False)
 is_favourite = models.BooleanField(default=False)