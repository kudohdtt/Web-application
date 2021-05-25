# Generated by Django 3.1.3 on 2020-12-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201214_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='number_of_room',
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=100),
        ),
    ]
