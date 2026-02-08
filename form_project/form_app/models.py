from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AuthUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"

class EmployeeModel(models.Model):
    STATUS = [
        ('Active','Active'),
        ('InActive','InActive')
    ]
    name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='hello')
    image = models.ImageField(upload_to='employee_img', null=True)
    status = models.CharField(choices=STATUS, max_length=100,null=True)
    joining_date = models.DateField(null=True)

    def __str__(self):
        return self.name
    
class SalaryModel(models.Model):
    STATUS = [
        ('Paid','Paid'),
        ('Unpaid','Unpaid')
    ]    
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name='emp_salary', null=True)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    month = models.CharField(max_length=100, null=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)
    bonus = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.employee.name}"