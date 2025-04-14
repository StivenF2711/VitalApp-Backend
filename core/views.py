from django.shortcuts import render

from rest_framework import viewsets
from .models import Core
from .serializers import CoreSerializer


class CoreViewSet(viewsets.ModelViewSet):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer
