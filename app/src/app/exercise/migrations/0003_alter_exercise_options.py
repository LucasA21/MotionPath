# Generated by Django 5.0.4 on 2024-06-06 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['name'], 'verbose_name': 'Ejercicio', 'verbose_name_plural': 'Ejercicios'},
        ),
    ]
