# Generated by Django 5.0.7 on 2024-07-29 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizado',
            name='CPF',
            field=models.CharField(max_length=100, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='autorizado',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.setor', verbose_name='Setor'),
        ),
    ]
