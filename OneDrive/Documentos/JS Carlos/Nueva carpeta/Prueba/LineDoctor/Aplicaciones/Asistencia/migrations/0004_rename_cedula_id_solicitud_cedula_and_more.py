# Generated by Django 5.1.1 on 2024-09-11 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0003_rename_cedula_solicitud_cedula_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='cedula_id',
            new_name='cedula',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='especialidad_id',
            new_name='especialidad',
        ),
    ]