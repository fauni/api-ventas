# Generated by Django 4.2 on 2023-04-20 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_movimientostock_descrpcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientostock',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]