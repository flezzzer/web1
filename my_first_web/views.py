from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    courses = models.Course.objects.all()
    return render(request, 'courses.html', {'courses':courses})

