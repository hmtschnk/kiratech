from django.contrib import admin
from django.urls import path
from .views import get_api

app_name = "api"

urlpatterns = [
    path('inventory', get_api, name="get_api"),
]
