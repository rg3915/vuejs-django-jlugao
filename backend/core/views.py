from django.shortcuts import render
from rest_framework import viewsets
from .models import Links
from .serializers import LinksSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
