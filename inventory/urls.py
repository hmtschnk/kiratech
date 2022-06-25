from django.contrib import admin
from django.urls import path
from .views import index, search_by_id

app_name = "inventory"

urlpatterns = [
    path('', index, name="index"),
    path('<id>/', search_by_id, name="search_by_id"),
]
