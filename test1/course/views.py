from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse("Hello django")

def learn_python(request):
    return HttpResponse('<h1> Hello python</h1>')


def learn_syllabus(request):
    a = '<h1> Python and django courses are available</h1>'
    return HttpResponse(a)