from .models import Paciente, PacientePhone, Phone
from rest_framework import viewsets, permissions
from .serializers import PacienteSerializer, PhoneSerializer, PacientePhoneSerializer, PacienteNumberSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

class PacienteNumberViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteNumberSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PhoneSerializer

class PacientePhoneViewSet(viewsets.ModelViewSet):
    queryset = PacientePhone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacientePhoneSerializer

