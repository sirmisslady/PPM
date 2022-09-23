from dataclasses import fields
from rest_framework import serializers
from .models import Paciente, Phone, PacientePhone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'number')
        depth = 1

class PacientePhoneSerializer(serializers.ModelSerializer):
    phone_number = serializers.ReadOnlyField(source="phone.number")
    class Meta:
        model = PacientePhone
        #fields = '__all__'
        fields = ('id', 'active', 'paciente', 'phone', 'phone_number')

class PacienteSerializer(serializers.ModelSerializer):
    #paciente_phones = PacientePhoneSerializer(many=True, source="pacientephone_set")
    class Meta:
        model = Paciente
        fields = ('id', 'nombre')

class PacienteNumberSerializer(serializers.ModelSerializer):
    paciente_phones = PacientePhoneSerializer(many=True, source="pacientephone_set")
    class Meta:
        model = Paciente
        fields = ('id', 'nombre', 'paciente_phones')