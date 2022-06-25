from django.contrib import admin
from django.urls import path
from .views import inv_view

app_name = "api"

urlpatterns = [
    path('inventory', inv_view.as_view(), name="inv"),
    path('inventory/<int:id>', inv_view.as_view(), name="inv_2"),
]
