from django.shortcuts import render,redirect
from .models import DepartmentModel,EmployeeModel,AuthUserModel,SalaryModel
from .forms import DepartmentForm,EmployeeForm,SalaryForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home_page(request):

    return render(request, 'home.html')

def register_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        user_exists = AuthUserModel.objects.filter(username=username)
        if user_exists:
            messages.warning(request,'User already exists')
            return redirect('login_page')
        if password == password_confirm:
            AuthUserModel.objects.create_user(
                full_name = full_name,
                username = username,
                email = email,
                password = password
            )
            return redirect('login_page')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('home_page') 
        else:
            messages.warning(request, 'Invalid Credentials.Please put right credentials')
            return redirect('login_page')
        
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
           
    return redirect('login_page')

def department_list(request):

    dept_data = DepartmentModel.objects.all()
    context_dict = {
        'dept_data':dept_data,
    }
    return render(request, 'department_list.html',context_dict)

@login_required
def add_department(request):
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        if dept_form.is_valid():
            dept_form.save()
            return redirect('department_list')
    dept_form = DepartmentForm()
    context_dict = {
        'dept_form':dept_form,
    }    
    return render(request, 'add_department.html',context_dict)

@login_required
def edit_department(request,pk):
    dept_data = DepartmentModel.objects.get(id = pk)
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST, instance=dept_data)
        if dept_form.is_valid():
            dept_form.save()
            return redirect('department_list')
        
    dept_form = DepartmentForm(instance=dept_data)
    context_dict = {
        'dept_form':dept_form,
    }
    return render(request,'edit_department.html',context_dict)

@login_required
def delete_department(request,pk):

    DepartmentModel.objects.get(id = pk).delete()
    return redirect('department_list')

def employee_list(request):
    employee_data = EmployeeModel.objects.all()
    context_dict = {
        'employee_data':employee_data
    }
    return render(request,'employee_list.html',context_dict)

def add_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('employee_list')

    employee_form = EmployeeForm()
    context_dict = {
        'employee_form':employee_form,
    }
    return render(request, 'add_employee.html',context_dict)

def edit_employee(request, emp_id):
    employee_data = EmployeeModel.objects.get(id = emp_id)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee_data)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('employee_list')
        
    employee_form = EmployeeForm(instance=employee_data)   
    context_dict = {
        'employee_form':employee_form,
    } 
    return render(request,'edit_employee.html',context_dict)

def delete_employee(request, emp_id):

    EmployeeModel.objects.get(id = emp_id).delete()

    return redirect('employee_list')

def salary_list(request):
    salary_data = SalaryModel.objects.all()

    context_dict = {
        'salary_data':salary_data
    }
    return render(request,'salary_list.html',context_dict)

def add_salary(request):
    if request.method == 'POST':
        salary_form = SalaryForm(request.POST)
        if salary_form.is_valid():
            salary = salary_form.save(commit=False)
            salary.status = 'Paid'
            salary.total_salary = salary.basic_salary + salary.bonus
            salary.save()
            return redirect('salary_list')
        
    salary_form = SalaryForm()
    context_dict = {
        'salary_form':salary_form,
    }
    return render(request, 'add_salary.html',context_dict)

def edit_salary(request,salary_id):
    salary_data = SalaryModel.objects.get(id = salary_id)
    if request.method == 'POST':
        salary_form = SalaryForm(request.POST, instance=salary_data)
        if salary_form.is_valid():
            salary = salary_form.save(commit=False)
            salary.status = 'Paid'
            salary.total_salary = salary.basic_salary + salary.bonus
            salary.save()
            return redirect('salary_list')
        
    salary_form = SalaryForm(instance=salary_data)
    context_dict = {
        'salary_form':salary_form,
    }
    return render(request, 'edit_salary.html',context_dict)

def delete_salary(request,salary_id):
    SalaryModel.objects.get(id = salary_id).delete()
    return redirect('salary_list')
