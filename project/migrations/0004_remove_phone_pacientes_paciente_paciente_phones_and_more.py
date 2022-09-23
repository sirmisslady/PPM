# Generated by Django 4.1.1 on 2022-09-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='pacientes',
        ),
        migrations.AddField(
            model_name='paciente',
            name='paciente_phones',
            field=models.ManyToManyField(through='project.PacientePhone', to='project.phone'),
        ),
        migrations.AlterField(
            model_name='pacientephone',
            name='active',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
