from django.shortcuts import render

# Create your views here.
def listfunction(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Mango']
    students = ['Jiya', 'Priya', 'Harry', 'Ron', 'Jasmin', 'John', 'Julia']
    ordered_students = []
    for s in students:
        if s.startswith("J"):
            ordered_students.append(s)
    return render(request, 'listapp.html', {'fruits':fruits, 'stdn':ordered_students})