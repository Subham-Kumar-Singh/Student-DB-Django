from django.shortcuts import render, redirect
# from django.views import view
from django.http import HttpResponse
from .models import *

from .form import *


def HomeFunc(request):
    stud = Student.objects.all()
    context = {'stud': stud}
    return render(request, 'core/home.html', context)


def addFunc(request):
    fm = AddStudentForm()

    if request.method == 'POST':
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    context = {'fm': fm}

    return render(request, 'core/add.html', context)


def deleteForm(request, pk):

    stud = Student.objects.get(id=pk)

    if request.method == 'POST':
        stud.delete()
        return redirect('/')

    context = {'stud': stud}
    return render(request, 'core/delete.html', context)


def updateForm(request, pk):

    stud = Student.objects.get(id=pk)

    fm = AddStudentForm(instance=stud)
    if request.method == 'POST':
        fm = AddStudentForm(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    context = {'fm': fm}

    return render(request, 'core/add.html', context)

# Create your views here.
