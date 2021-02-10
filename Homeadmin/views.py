from django.shortcuts import render,redirect
from django.views.generic import View,ListView,UpdateView
from .models import AddEmployeeModel
# Create your views here.
def checkLogin(request):
    name=request.POST['login']
    password=request.POST['login']
    if name=='admin' and password=='admin':
        return render(request, "admin/AdminHome.html")
    else:
        massage="Plase Give valid Input"
        return render(request, "admin/adminlogin.html", {"data": "Plase Give valid Input"})


class AddEmployee(View):
    def get(self,request):
        return render(request,"admin/AddEmployee.html")
    def post(self,request):
        name=request.POST['first_name']
        lastname=request.POST['last_name']
        password=request.POST['password']
        gender=request.POST['gender']
        email=request.POST['email']
        mobile = request.POST['mobile']
        designations = request.POST['designations']
        address = request.POST['address']
        try:
            if AddEmployeeModel.objects.get(contactno=mobile):
                msg="Mobile number is available"
        except AddEmployeeModel.DoesNotExist:
                AddEmployeeModel(name=name, lastName=lastname, password=password, gender=gender, email=email, contactno=mobile,
                                 designations=designations, address=address).save()
                msg="Employee data is save.."
        return render(request, "admin/AddEmployee.html",{"msg":msg} )


class ViewEmployee(ListView):
    model = AddEmployeeModel
    fileds = "__all__"
    template_name = 'admin/viewEmployee.html'


class ShowEmployee(ListView):
    model = AddEmployeeModel
    fileds = "__all__"
    template_name = 'admin/showEmployee.html'


def UpdateEmployee(request):
    id = request.GET.get("id")
    print(id)
    # result = Employee.objects.filter(idno=id) # Will return QuerySet
    result = AddEmployeeModel.objects.get(id=id)
    return render(request,"admin/Update_save.html",{"info":result})


def saveupdate(request):
    id=request.POST.get("id")
    first_name=request.POST.get("first_name")
    print(first_name)
    last_name=request.POST.get("last_name")
    password=request.POST.get("password")
    email=request.POST.get("email")
    mobile=request.POST.get("mobile")
    designations=request.POST.get("designations")
    address=request.POST.get("address")
    AddEmployeeModel(id=id,name=first_name,lastName=last_name,password=password,email=email,contactno=mobile,designations=designations,address=address).save()
    return redirect("ViewEmployee")


class DeleteEmployee(View):
    def get(self,request):
        delete=AddEmployeeModel.objects.all()
        return render(request, "admin/deleteEmployee.html",{"delete":delete})
    def post(self,request):
        delete = AddEmployeeModel.objects.all()
        id= request.POST.getlist("selet")
        for x in id:
           print(x)
           y=int(x)
           AddEmployeeModel.objects.filter(id=y).delete()
           return render(request,"admin/deleteEmployee.html",{"msg":"records are Deleted Successsfully","delete":delete})

