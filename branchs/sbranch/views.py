from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>hello! We in the second branch app!</h1>')

# Create your views here.
