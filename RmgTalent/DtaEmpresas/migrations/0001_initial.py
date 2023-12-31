# Generated by Django 4.2.6 on 2023-11-26 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('idEmp', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='Número de NIT/RUT')),
                ('nomEmp', models.CharField(max_length=200, verbose_name='Nombre Empresa')),
                ('encarEmp', models.CharField(max_length=200, verbose_name='Nombre de representante')),
                ('sectEmp', models.CharField(max_length=50, verbose_name='Sector')),
                ('dirEmp', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telEmp', models.CharField(blank=True, max_length=10, null=True, verbose_name='Tel. Contacto')),
                ('mailEmp', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo Electronico')),
                ('logoEmp', models.ImageField(blank=True, default='null', null=True, upload_to='Empresa', verbose_name='Imagen')),
                ('pubEmp', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('creaEmp', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('actuEmp', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('tipoDoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.tipodoc', verbose_name='Tipo de Documento')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
