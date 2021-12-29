from django.contrib import admin
from django.urls import path, include
import oauth2_provider.views as oauth2_views

oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace="oauth2_provider"))
]
