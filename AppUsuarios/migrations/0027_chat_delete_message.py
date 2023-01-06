# Generated by Django 4.1.3 on 2023-01-05 00:40

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUsuarios', '0026_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tiempo', models.DateField(blank=True, null=True)),
                ('leido', models.BooleanField(default=False)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrada', to=settings.AUTH_USER_MODEL)),
                ('salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salida', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]