from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def datetimeview(request):
    now = datetime.now()
    html = "<html><Body>The current date and time is %s.</body></html>" %now
    return HttpResponse(html)

def dateview(request):
    now = datetime.now()
    html = "<html><Body>The current date is %s.</body></html>" %now.date()
    return HttpResponse(html)

def timeview(request):
    now = datetime.now()
    html = "<html><Body>The current time is %s.</body></html>" %now.time()
    return HttpResponse(html)