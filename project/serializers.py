from rest_framework import serializers
from .models import Paciente

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id', 'nombre')
        #read_only_fields = (')