from django.shortcuts import render
# from django.views import view
from django.http import HttpResponse
from .models import *


def HomeFunc(request):
    stud = Student.objects.all()
    context = {'stud': stud}
    return render(request, 'core/home.html', context)


# Create your views here.
