from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def token(request):
    return HttpResponse("Oauth Token")