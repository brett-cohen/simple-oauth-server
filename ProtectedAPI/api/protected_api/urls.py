from django.urls import path

from .views import RandomEndpoint

urlpatterns = [
    path('random', RandomEndpoint.as_view())
]