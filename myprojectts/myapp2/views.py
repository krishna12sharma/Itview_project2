from django.shortcuts import render,redirect
from .models import Student
from.forms import StudentForm
# Create your views here.

#Load form
def studentForm(request):
    return render(request,'student_form.html')

#Note:-By default the <form >has GEt method always
def addData(request):
    # vname = request.GET['sname'] #fetch value from the textbox using GET method
    # vname=request.POST['sname']  #fetch value from the textbox using POST method
    vname = request.POST.get('sname') #fetch value from the textbox and has both POST and GET method
    print(vname)
    vgender=request.POST.get('gender')
    vhobbies=request.POST.getlist('hobbies[]')
    vcountry=request.POST.get('country')
    return render(request, 'result.html',{'sname':vname,'gender':vgender,'hobbies':vhobbies,'country':vcountry})

def showData(request):
    obj=Student.objects.all() #fetch the records
    return render(request,'showEmployee.html',{'data':obj})


def loadModelForm(request):
    stdForm=StudentForm()#object of model form
    return render(request,'myform.html',{'myform':stdForm})
