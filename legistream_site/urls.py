from django.contrib import admin
from django.urls import path, include
from . import secrets

urlpatterns = [
    path(secrets.ADMIN_PATH, admin.site.urls),
    path('', include('legistream.urls')),
]
