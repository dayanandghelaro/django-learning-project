from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, World!")
    return render(request, "hello/index.html")

def dayanand(request):
    return HttpResponse("Hello Dayanand!")

def greet(request, name):
    #return HttpResponse(f"Hello {name.capitalize()}!")
    return render(request, "hello/greet.html",{
        'name':name.capitalize()
    })
