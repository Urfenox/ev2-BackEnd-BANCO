# Generated by Django 4.1 on 2022-11-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gerencia', '0002_alter_solicitud_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_ingreso',
            field=models.DateField(default='2022-11-16'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
