# Generated by Django 4.1.7 on 2023-02-26 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicgen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicscorerecord',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
    ]