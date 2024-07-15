from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Stud, Course

# Create your views here.
def index(request):
    context = {
        'num_students' : Stud.objects.count(),
        'num_courses' : Course.objects.count(),
    }
    return render(request, 'index.html', context)

class StudentListView(ListView):
    model = Stud
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Stud
    template_name = 'student_detail.html'
    context_object_name = 'students'

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'courses'