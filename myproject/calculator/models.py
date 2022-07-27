from django.db import models

# Create your models here.
class Cal(models.Model):
    first_value= models.CharField(max_length=50)
    second_value = models.CharField(max_length=20)
    result = models.CharField(max_length=30)