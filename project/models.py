from django.db import models

# Create your models here.


class Phone(models.Model):
    number = models.CharField(max_length=15)
    #pacientes = models.ManyToManyField(Paciente, through='PacientePhone')

    def __str__(self):
        return self.number

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_pat = models.CharField(max_length=50,default=None)
    apellido_mat = models.CharField(max_length=50,default=None)
    direccion = models.CharField(max_length=200,default=None)
    paciente_phones = models.ManyToManyField(Phone, through='PacientePhone')

    def __str__(self):
        return self.nombre

class PacientePhone(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    active = models.BooleanField()