from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.portal, name='index'),
    path('apply/', views.apply, name='apply'),
    path('register/',views.register, name='register'),
    path('view_resume/', views.view_resume, name='view_resume'),
    path('resume_list/', views.resume_list, name='resume_list'),
    path('resume/<int:session_id>/', views.view_resume, name='view_resume'),
    path('portal/', views.portal, name='portal'),
    path('pyapply/', views.pyapply, name='pyapply'),
    path('greet/', views.greet, name='greet'),
    path('pylist/', views.pylist, name='pylist'),
    path('view_resume2/<int:session_id>/', views.view_resume2, name='view_resume2'),
    path('greet2/', views.greet2, name='greet2'),
]
