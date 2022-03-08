from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Checking work</h4>")

def about(request):
    return HttpResponse("<h4>I'm very smart!</h4>")