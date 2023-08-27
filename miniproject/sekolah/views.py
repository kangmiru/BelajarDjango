from django.shortcuts import render

from rest_framework import viewsets

from .models import Siswa, Guru
from .serializers import SiswaSerializer, GuruSerializer

# Create your views here.
class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer

class GuruViewSet(viewsets.ModelViewSet):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer