# Generated by Django 4.1 on 2022-08-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha_medica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.IntegerField(unique=True)),
                ('vacunas', models.CharField(blank=True, max_length=100, null=True)),
                ('desparasitacion', models.CharField(blank=True, max_length=50, null=True)),
                ('castracion', models.CharField(blank=True, max_length=50, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('especie', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=20)),
                ('edad_aprox', models.IntegerField()),
                ('ingreso', models.DateField()),
                ('observaciones', models.TextField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
