from django.db import models

# Create your models here.

class User(models.Model):
    image = models.ImageField(upload_to='user/')
    frist_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    work = models.CharField(max_length=150)