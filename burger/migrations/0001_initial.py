# Generated by Django 5.0 on 2024-01-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=40)),
                ('sucursal', models.CharField(max_length=40)),
                ('bebida', models.CharField(max_length=40)),
                ('hamburguesa', models.CharField(max_length=40)),
                ('cant_blends', models.CharField(max_length=40)),
                ('cant_hamburguesas', models.IntegerField()),
                ('metodo_pago', models.CharField(max_length=40)),
                ('observacion', models.TextField()),
            ],
        ),
    ]
