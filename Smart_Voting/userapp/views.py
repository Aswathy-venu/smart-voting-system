from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def uregister(request):
    # return HttpResponse("Hello World!")
    return render(request,"User/uregister.html")
def ulogin(request):
    # return HttpResponse("Hello World!")
    return render(request,"User/ulogin.html")
