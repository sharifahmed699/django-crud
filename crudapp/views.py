from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index (request):
    employes = Employee.objects.all()
    return render (request, "index.html", {'employes': employes})

def createEmployee(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  
            except:
                pass      
    else:
        form = EmployeeForm()
        return render(request,"createEmployee.html", {'form':form})


def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,"edit.html", {'employee': employee})  


def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, "edit.html", {'employee': employee}) 


def delete(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect('/')  