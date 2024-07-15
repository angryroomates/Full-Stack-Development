from django.shortcuts import render, get_object_or_404, redirect
from .models import Stud, Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_details(request, course_id):
    coursedb = get_object_or_404(Course, id=course_id)
    students = coursedb.students.all()
    return render(request, 'course_details.html', {'course': coursedb, 'students': students})

def student_register(request, course_id):
    coursedb = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        joining_date = request.POST.get('joining_date')

        if fname and lname and email and joining_date:
            student, created = Stud, objects.get_or_created(email = email, defaults = {'fname': fname, 'lname':lname, 'joining_date':joining_date})
            coursedb.students.add(student)
            return redirect("course_details", course_id=coursedb.id)
    return render(request, "student_register.html", {"course":coursedb})