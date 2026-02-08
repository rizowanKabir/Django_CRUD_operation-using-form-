from django.contrib import admin
from .models import DepartmentModel,EmployeeModel,AuthUserModel,SalaryModel

# Register your models here.

admin.site.register([DepartmentModel,EmployeeModel])
admin.site.register(AuthUserModel) 
admin.site.register(SalaryModel)