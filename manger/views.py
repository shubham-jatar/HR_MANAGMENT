from django.shortcuts import render

# Create your views here.
def managerHome(request):
    return render(request, "manager/managerLogin.html")


def managerLogin(request):
    username=request.POST.get("username")
    password=request.POST.get("pass")
    print(username)
    print(password)
    if username=="manager" and password=="manager":
        return render(request,"manager/managerHomepage.html")
    else:
        return render(request,"manager/managerLogin.html",{"msg":"Invalid Input"})

    return None


def recrutment(request):
    return render(request,"manager/recrutmentmain.html")


def newRecuirtment(request):
    return render(request,"manager/newrecrutment.html")


def managerHomepage(request):
    return render(request,"manager/managerHomepage.html")