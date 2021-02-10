from django.db import models

# Create your models here.
class AddEmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email=models.EmailField()
    designations = models.CharField(max_length=30,default=False)
    address = models.CharField(max_length=40)
    contactno = models.IntegerField(unique=True)
    save=models.CharField(default=True,max_length=20)

