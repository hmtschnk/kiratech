from django.contrib import admin
from django.urls import path
from .views import index, search, search_by_id

app_name = "inventory"

urlpatterns = [
    path('', index, name="index"),
    path('search', search, name="search"),
    path('<id>/', search_by_id, name="search_by_id"),
]
