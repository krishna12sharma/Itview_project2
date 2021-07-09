from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def loadForm(request):
    empfrm=EmployeeForm()
    return render(request,'employee.html',{'myform':empfrm})

#insert values into
def insertEmployee(request):
    if request.method=='POST':
        empform=EmployeeForm(request.POST) #creates object of EMployee Form and uses post
        if(empform.is_valid()):
            empform.save()
    return redirect('/showEmployee') #we use the urlname

def showEmployee(request):
    # emp=Employee.objects.all()
    emp = Employee.objects.raw("select * from crudapp_Employee")
    return render(request,'showEmployee.html',{'data':emp})


def deleteEmployee(request,eid):
    emp=Employee.objects.get(id=eid) #Get the id of the particualr record
    emp.delete()
    return redirect('/showEmployee')

def updateEmployee(request,eid):
    if request.method=='POST':
        emp=Employee.objects.get(id=eid)
        frm=EmployeeForm(request.POST,instance=emp) #gives values in the textbox
        if(frm.is_valid()):
            frm.save()
            return redirect('/showEmployee')

    else:
        emp = Employee.objects.get(id=eid)
        frm = EmployeeForm(instance=emp)
        return render(request,'editEmployee.html',{'form':frm})
















