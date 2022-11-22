# Generated by Django 4.1.1 on 2022-10-02 02:34

from django.db import migrations, models
import inventario.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[inventario.validators.validate_email])),
                ('ubicacion', models.TextField()),
                ('tarjeta', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='OrdenPedido',
            new_name='PedidoProducto',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, validators=[inventario.validators.validar_nombre_categoria]),
        ),
    ]
