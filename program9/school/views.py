from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Stud, Course

import csv
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def index(request):
    context = {
        'num_students' : Stud.objects.count(),
        'num_courses' : Course.objects.count(),
    }
    return render(request, 'index.html', context)

def generate_student_csv(request):
    students = Stud.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Joining Date'])

    for s in students:
        writer.writerow([s.fname, s.lname, s.email, s.joining_date])
    return response

def generate_course_csv(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Course Name', 'Course Description'])

    for c in courses:
        writer.writerow([c.course_name, c.description])
    return response

def render_to_pdf(template_src, context_dic={}):
    template = get_template(template_src)
    html= template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_student_pdf(request):
    students = Stud.objects.all()
    context = {'students': students}
    pdf = render_to_pdf('student_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def generate_course_pdf(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    pdf = render_to_pdf('courses_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

class StudentListView(ListView):
    model = Stud
    template_name = 'student_list.html'
    context_object_name = 'students'

#class StudentDetailView(DetailView):
#    model = Stud
#    template_name = 'student_detail.html'
#    context_object_name = 'students'

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

#class CourseDetailView(DetailView):
#    model = Course
#    template_name = 'course_detail.html'
#    context_object_name = 'courses'