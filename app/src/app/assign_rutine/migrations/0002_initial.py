# Generated by Django 5.0.4 on 2024-05-29 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assign_rutine', '0001_initial'),
        ('rutine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignrutine',
            name='rutine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rutine.rutine'),
        ),
    ]