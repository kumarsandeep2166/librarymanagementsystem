from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('master1/',views.master1, name='master1'),
    path('master2/',views.master2, name='master2'),
    path('master3/',views.master3, name='master3'),
    path('profile_create/',views.profile_create, name='profile_create'),
    
    path('profilepage/',views.profilepage, name='profilepage'),
    path('profile_edit/<int:pk>/',views.profile_edit, name='profile_edit'),
    path('profile_list/<int:pk>/',views.profile_delete, name='profile_delete'),
    path('coursesetup/',views.coursesetup, name='coursesetup'),
    
    path('stream_create/',views.stream_create, name='stream_create'),
    path('stream_list/',views.stream_list, name='stream_list'),
    path('stream_edit/<int:pk>',views.stream_edit, name='stream_edit'),
    path('stream_delete/<int:pk>',views.stream_delete, name='stream_delete'),

    path('course_create/',views.course_create, name='course_create'),
    path('course_list/',views.course_list, name='course_list'),
    path('course_edit/<int:pk>',views.course_edit, name='course_edit'),
    path('course_delete/<int:pk>',views.course_delete, name='course_delete'),

    path('year_sem_create/',views.year_sem_create, name='year_sem_create'),
    path('year_sem_list/',views.year_sem_list, name='year_sem_list'),
    path('year_sem_edit/<int:pk>',views.year_sem_edit, name='year_sem_edit'),
    path('year_sem_delete/<int:pk>',views.year_sem_delete, name='year_sem_delete'),

    path('profile/', views.profile, name='profile')
]