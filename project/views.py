from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project.models import Paciente, Phone
from .serializers import PacienteSerializer, PhoneSerializer

# Create your views here.

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer

    def get_queryset(self):
        paciente = Paciente.objects.all()
        return paciente


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        phone = Phone.objects.all()
        return phone
