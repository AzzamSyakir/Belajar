from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    
class book(models.Model):
    bookname=models.CharField(max_length=10)
