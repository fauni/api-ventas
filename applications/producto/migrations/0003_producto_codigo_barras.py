# Generated by Django 4.2 on 2023-04-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_categoria_grupo_producto_tipomovimiento_proveedor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(default=0, max_length=13),
        ),
    ]
