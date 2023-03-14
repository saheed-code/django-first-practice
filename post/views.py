from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return render(request, "post/hello.html")


def greet(request):
    return HttpResponse("Hello Cohort 13")


def work(request):
    return render(request, "post/work.html")
