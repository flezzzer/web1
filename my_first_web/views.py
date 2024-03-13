import http.client

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models

# Create your views here.

def index(request):
    courses = models.Course.objects.all()
    return render(request, 'my_first_web/courses.html', {'courses': courses})


def single_course(request, course_id):
    course = get_object_or_404(models.Course, pk=course_id)
    return render(request, 'my_first_web/single_course.html', {'course': course})
