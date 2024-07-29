from django.shortcuts import render, get_object_or_404, redirect
from .models import Stud, Course
from django.http import JsonResponse

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
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        joining_date = request.POST.get('joining_date')

        if fname and lname and email and joining_date:
            student, created = Stud.objects.get_or_create(
                email=email, defaults={'fname': fname, 'lname': lname, 'joining_date': joining_date}
            )
            if not created:
                return JsonResponse({'success': False, 'error': 'Student with this email already exists.'})
            coursedb.students.add(student)
            return JsonResponse({'success': True, 'student': {'fname': student.fname, 'lname': student.lname}})
        return JsonResponse({'success': False, 'error': 'All fields are required.'})
    return render(request, 'student_register.html', {'course': coursedb})

def search_student(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '').strip()
        if query:
            students = Stud.objects.filter(fname__icontains=query) | Stud.objects.filter(lname__icontains=query)
            results = []
            for student in students:
                courses = student.courses.all()
                course_names = [course.course_name for course in courses]
                results.append({'student': f"{student.fname} {student.lname}", 'courses': course_names})
            return JsonResponse({'results': results})
    return render(request, 'search_student.html')