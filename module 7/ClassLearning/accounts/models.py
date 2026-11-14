from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField()
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField( max_length=50)
    father_name = models.CharField( max_length=50)
    mother_name = models.CharField( max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    monthly_fee = models.IntegerField()
    address = models.TextField()
    bio = models.TextField()