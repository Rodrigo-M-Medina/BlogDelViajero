# Generated by Django 4.1.3 on 2023-01-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0012_imagenperfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='subtitulo_posteo',
            field=models.CharField(default='hola', max_length=40),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='titulo_posteo',
            field=models.CharField(max_length=40),
        ),
    ]
