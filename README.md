# Employee Management System

A comprehensive web-based Employee Management System built with Django that allows organizations to manage departments, employees, and salary information efficiently.

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Features

- **User Authentication**
  - User registration with custom user model
  - Secure login/logout functionality
  - Password-protected access to sensitive operations

- **Department Management**
  - Create, read, update, and delete departments
  - Department description and details
  - View all departments in a list

- **Employee Management**
  - Add new employees with detailed information
  - Upload employee profile images
  - Track employee status (Active/Inactive)
  - Record joining dates and designations
  - Edit and delete employee records
  - Associate employees with departments

- **Salary Management**
  - Manage employee salaries with basic pay and bonuses
  - Track salary status (Paid/Unpaid)
  - Automatic total salary calculation
  - Monthly salary records
  - Edit and update salary information

## 🛠️ Technology Stack

- **Backend:** Django 4.x
- **Database:** SQLite (default) / PostgreSQL / MySQL
- **Frontend:** HTML, CSS
- **Authentication:** Django Auth System
- **Forms:** Django Forms

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ``
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
employee-management-system/
│
├── app_name/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── department_list.html
│   │   ├── add_department.html
│   │   ├── edit_department.html
│   │   ├── employee_list.html
│   │   ├── add_employee.html
│   │   ├── edit_employee.html
│   │   ├── salary_list.html
│   │   ├── add_salary.html
│   │   └── edit_salary.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## 🗄️ Database Models

### AuthUserModel
- Custom user model extending Django's AbstractUser
- Fields: full_name, username, email, password

### DepartmentModel
- name: Department name
- description: Department description

### EmployeeModel
- name: Employee name
- designation: Job title
- department: Foreign key to DepartmentModel
- image: Employee profile picture
- status: Active/Inactive
- joining_date: Date of joining

### SalaryModel
- employee: Foreign key to EmployeeModel
- basic_salary: Base salary amount
- month: Salary month
- status: Paid/Unpaid
- bonus: Additional bonus amount
- total_salary: Calculated total (basic + bonus)

## 🔒 Authentication & Authorization

- Login required for most operations
- Custom user model with extended fields
- Session-based authentication
- Protected routes using `@login_required` decorator

## 🚀 Usage

### Register a New User
1. Navigate to the registration page
2. Fill in the required details (full name, username, email, password)
3. Click register to create an account

### Manage Departments
1. Login to your account
2. Navigate to "Departments"
3. Add, edit, or delete departments as needed

### Manage Employees
1. Go to "Employees" section
2. Click "Add Employee" to create new employee records
3. Upload profile images and assign to departments
4. Edit or remove employee records

### Manage Salaries
1. Access "Salary" section
2. Add salary records for employees
3. System automatically calculates total salary (basic + bonus)
4. Track payment status

## 📝 Requirements.txt

```
Django>=4.0,<5.0
Pillow>=9.0.0
```

## 🔧 Future Enhancements

- [ ] Add role-based permissions (Admin, HR, Manager)
- [ ] Generate salary slips in PDF format
- [ ] Employee attendance tracking
- [ ] Leave management system
- [ ] Dashboard with analytics and reports
- [ ] Email notifications for salary payments
- [ ] Export data to Excel/CSV
- [ ] Advanced search and filtering
- [ ] Employee performance reviews
- [ ] API endpoints for mobile app integration




