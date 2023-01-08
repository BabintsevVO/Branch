from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hii. now we have 2 branchs</h1>')

# Create your views here.
