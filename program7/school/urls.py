from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_project/', views.register_student_project, name='register_student_project'),
    path('students/',views.student_list, name='student_list'),
]