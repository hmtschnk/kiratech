from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventory.models import inventory
from .api import inv_serializer

# Create your views here.
class inv_view(APIView):
    def get(self, request, id=None):
        if id:
            item = inventory.objects.get(name=id)
            serializer = inv_serializer(item)
            inv = serializer.data
            return Response({"data": inv}, status=status.HTTP_200_OK)

        items = inventory.objects.all()
        serializer = inv_serializer(items, many=True)
        inv = serializer.data
        return Response({"data": inv}, status=status.HTTP_200_OK)