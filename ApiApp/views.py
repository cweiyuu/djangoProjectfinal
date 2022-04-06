from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serialzers import ProductModelSerializer
from .models import ProductModel

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all().order_by('id')
    serializer_class = ProductModelSerializer
