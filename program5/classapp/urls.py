from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name="course_list"),
    path('course/<int:course_id>/',views.course_details, name='course_details'),
    path('course/<int:course_id>/register',views.student_register, name='studentRegister'),
]