from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello Dog Collector</h1>')

def about(request):
    return HttpResponse('<h1>About the Dog Collector</h1>')