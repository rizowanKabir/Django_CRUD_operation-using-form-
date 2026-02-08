from django import forms
from .models import DepartmentModel,EmployeeModel,SalaryModel

# Create forms here.

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields = '__all__' 
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'   
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Enter Your name'}),
            'designation': forms.TextInput(attrs={'placeholder':'Enter Your designation'}),
            'joining_date' : forms.DateInput(attrs={'type':'date'})
        }    

class SalaryForm(forms.ModelForm):
    class Meta:
        model = SalaryModel
        fields = '__all__'
        exclude = ['status','total_salary']      

