# Generated by Django 4.1.3 on 2022-12-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0004_alter_posteo_contenido_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='imagen_posteo',
            field=models.ImageField(default=3, upload_to='Imagen'),
            preserve_default=False,
        ),
    ]
