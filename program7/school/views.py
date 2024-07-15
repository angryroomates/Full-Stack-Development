from django.shortcuts import render, redirect
from .forms import StudForm
from .models import Stud, Project

# Create your views here.
def register_student_project(request):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudForm()
    return render(request, 'register_student_project.html', {'form':form})

def student_list(request):
    students= Stud.objects.all()
    return render(request, 'student_list.html', {'students':students})

def index(request):
    return render(request, 'index.html')
        