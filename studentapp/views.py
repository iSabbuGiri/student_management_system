from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from studentapp.EmailBackEnd import EmailBackEnd



# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")
    
def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed</h2>")  
    else:
        user =EmailBackEnd. authenticate(request, username= request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request,user)
            return HttpResponse("Email:" + request.POST.get("email") + "Password:" + request.POST.get("password")) 
        else:
            return HttpResponse("Invalid Login")     

def get_user_details(request):
    if request.user !=None:
        login(request,user)
        return HttpResponse("User:"+request.user.email+"usertype:"+request.user.user_type)
    else:
        return HttpResponse("Please Login First")    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")