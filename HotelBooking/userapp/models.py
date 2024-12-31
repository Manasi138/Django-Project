from django.db import models

class Customer(models.Model):
    emailId=models.AutoField(primary_key=True)
    C_name=models.CharField(max_length=100)
    C_password=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    aadhar_no=models.CharField(max_length=100)
    

# Create your models here.
