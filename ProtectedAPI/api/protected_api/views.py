from random import randrange
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def random(request):
    return HttpResponse(randrange(1, 10))