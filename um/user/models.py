from django.db import models

# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=150)
	phone=models.CharField(max_length=12)

