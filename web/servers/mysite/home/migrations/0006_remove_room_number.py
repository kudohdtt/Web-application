# Generated by Django 3.1.3 on 2020-12-13 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201214_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='number',
        ),
    ]