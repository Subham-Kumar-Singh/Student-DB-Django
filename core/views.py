from django.shortcuts import render
# from django.views import view
from django.http import HttpResponse

def HomeFunc(request):
    return render(request,'core/home.html')




# Create your views here.
