# Generated by Django 4.1.3 on 2023-01-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0036_rename_usuario_biografia_usuariobio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biografia',
            name='bio',
            field=models.CharField(max_length=800),
        ),
    ]
