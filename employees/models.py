from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    salary=models.IntegerField()
    image=models.ImageField(upload_to='employee_image')