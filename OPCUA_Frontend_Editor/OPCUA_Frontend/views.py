from django.shortcuts import render
from django.http import HttpResponse

def Frontend(request):
    return HttpResponse("Hello world!")