from random import randrange
from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView


# Create your views here.


class RandomEndpoint(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(randrange(1, 10))