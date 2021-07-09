from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Welcome to Django!!!!<h1>")
#

def home_function(request):

    name='John'
    n1,n2,n3=10,20,30
    list1=[10,203,'abc']
    return render(request,'home.html',{'sname':name,'n1':n1,'n2':n2,'n3':n3,'list':list1})

def about_function(request):
    return render(request,'about.html')
