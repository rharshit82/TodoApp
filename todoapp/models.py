from django.db import models
from datetime import datetime

class Todo(models.Model):
    title= models.CharField(max_length=60)
    desc= models.TextField()
    time = models.DateTimeField(default= datetime.now())
