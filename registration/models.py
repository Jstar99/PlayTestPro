from django.db import models

# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()

