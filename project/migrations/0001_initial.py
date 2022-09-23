# Generated by Django 4.1.1 on 2022-09-23 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_pat', models.CharField(default=None, max_length=50)),
                ('apellido_mat', models.CharField(default=None, max_length=50)),
                ('direccion', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PacientePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.paciente')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.phone')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='paciente_phones',
            field=models.ManyToManyField(through='project.PacientePhone', to='project.phone'),
        ),
    ]
