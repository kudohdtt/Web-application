# Generated by Django 3.1.3 on 2020-12-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=100),
        ),
    ]
