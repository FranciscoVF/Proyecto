# Generated by Django 3.1.4 on 2020-12-28 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Medicos', '0007_auto_20201228_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='apellido_m',
            field=models.CharField(help_text='Apellido materno', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
