from django.urls import path
from . import views

urlpatterns = [
    path('student_create/', views.student_create, name='student_create'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('student_delete/<int:pk>/', views.student_delete, name='student_delete'),
]