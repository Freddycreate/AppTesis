# Generated by Django 4.2.2 on 2023-06-20 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('molienda', '0002_alter_atomizado_barbotina_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atomizado',
            old_name='Barbotina',
            new_name='barbotina',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Codigo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Granulometria',
            new_name='granulometria',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Hora',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Humedad',
            new_name='humedad',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='NroSilo',
            new_name='nroSilo',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Observaciones',
            new_name='observaciones',
        ),
        migrations.RenameField(
            model_name='atomizado',
            old_name='Planta',
            new_name='planta',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Densidad',
            new_name='densidad',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Hora',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Planta',
            new_name='planta',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Residuo',
            new_name='residuo',
        ),
        migrations.RenameField(
            model_name='barbotina',
            old_name='Viscosidad',
            new_name='viscosidad',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Fecha',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Fondo',
            new_name='fondo',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Hora',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Malla180',
            new_name='malla180',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Malla300',
            new_name='malla300',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Malla425',
            new_name='malla425',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Malla500',
            new_name='malla500',
        ),
        migrations.RenameField(
            model_name='granulometria',
            old_name='Planta',
            new_name='planta',
        ),
        migrations.RenameField(
            model_name='planta',
            old_name='NroPlanta',
            new_name='nroPlanta',
        ),
    ]
