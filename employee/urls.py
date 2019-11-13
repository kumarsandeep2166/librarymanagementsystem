from django.urls import path
from . import views

urlpatterns = [
    path('emp_dept_create/', views.employee_department_create, name='emp_dept_create'),
    path('emp_dept_edit/<int:pk>/', views.employee_department_edit, name='emp_dept_edit'),
    path('emp_dept_list/', views.employee_department_list, name='emp_dept_list'),
    path('employee_designation_create/', views.employee_designation_create, name='employee_designation_create'),
    path('employee_designation_list/', views.employee_designation_list, name='employee_designation_list'),
    path('employee_designation_edit/<int:pk>/', views.employee_designation_edit, name='employee_designation_edit'),
    path('employee_create/', views.employee_create, name='employee_create'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee_delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]