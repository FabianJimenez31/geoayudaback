# Generated by Django 3.0.4 on 2020-04-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200401_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entidad',
            old_name='dirección',
            new_name='direccion',
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='entidad',
            name='longitud',
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='direccion',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='latitud',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='longitud',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
