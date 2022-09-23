from .models import Paciente, PacientePhone, Phone
from rest_framework import viewsets, permissions
from .serializers import PacienteSerializer, PhoneSerializer, PacientePhoneSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PhoneSerializer

class PacientePhoneViewSet(viewsets.ModelViewSet):
    queryset = PacientePhone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacientePhoneSerializer

