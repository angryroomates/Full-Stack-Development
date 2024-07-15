from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_student_csv/', views.generate_student_csv, name='generate_student_csv'),
    path('generate_course_csv/', views.generate_course_csv, name='generate_course_csv'),
    path('generate_student_pdf/', views.generate_student_pdf, name='generate_student_pdf'),
    path('generate_course_pdf/', views.generate_course_pdf, name='generate_course_pdf'),

    # Student-related views
    path('students/', views.StudentListView.as_view(), name='student_list'),
    #path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),

    # Course-related views
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    #path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
]