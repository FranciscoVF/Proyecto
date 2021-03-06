# Generated by Django 3.1.4 on 2020-12-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_pacientes_hora_atendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='descripcion',
            field=models.CharField(help_text='De que trato la colsulta y seguimiento que se dara', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='contacto',
            field=models.CharField(help_text='Manera por la cual nos podemos poner en contacto con paciente ya sea correo, celular o telefono de casa', max_length=255, null=True),
        ),
    ]
