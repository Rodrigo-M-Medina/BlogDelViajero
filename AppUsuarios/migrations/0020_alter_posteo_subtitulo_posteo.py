# Generated by Django 4.1.3 on 2023-01-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0019_alter_posteo_subtitulo_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='subtitulo_posteo',
            field=models.CharField(max_length=40),
        ),
    ]
