from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list/', views.department_list, name='department_list'),
    path('add_department/', views.add_department, name='add_department'),
    path('edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('delete/<int:pk>/', views.delete_department, name='delete_department'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('', views.home_page, name='home_page'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('salary_list/', views.salary_list, name='salary_list'),
    path('add_salary/', views.add_salary, name='add_salary'),
    path('edit_salary/<int:salary_id>/', views.edit_salary, name='edit_salary'),
    path('delete_salary/<int:salary_id>/', views.delete_salary, name='delete_salary'),
]