from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=200)

class Phone(models.Model):
    phone = models.CharField(max_length=15)

class Email(models.Model):
    email = models.CharField(max_length=200)

#class PhonePaciente():
    #phone_id = models.IntegerField