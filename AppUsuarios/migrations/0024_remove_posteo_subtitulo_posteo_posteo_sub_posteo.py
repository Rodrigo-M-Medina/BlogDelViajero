# Generated by Django 4.1.3 on 2023-01-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuarios', '0023_alter_posteo_subtitulo_posteo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='subtitulo_posteo',
        ),
        migrations.AddField(
            model_name='posteo',
            name='sub_posteo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
