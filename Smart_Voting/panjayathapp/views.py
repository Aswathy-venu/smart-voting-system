from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pregister(request):
    # return HttpResponse("Hello World!")
    return render(request,"panjayath/pregister.html")