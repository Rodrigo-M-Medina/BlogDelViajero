# Generated by Django 4.1.3 on 2023-01-04 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0013_posteo_subtitulo_posteo_alter_posteo_titulo_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='subtitulo_posteo',
            field=models.TextField(default='hola', max_length=40),
        ),
    ]
