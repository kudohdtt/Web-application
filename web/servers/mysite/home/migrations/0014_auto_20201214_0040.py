# Generated by Django 3.1.3 on 2020-12-13 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20201214_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='number',
            new_name='number_of_room',
        ),
    ]
