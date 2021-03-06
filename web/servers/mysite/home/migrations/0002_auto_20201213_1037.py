# Generated by Django 3.1.3 on 2020-12-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='acreage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='bed',
            field=models.CharField(default='1 Large bed', max_length=200),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='image',
            field=models.CharField(default='/static/templates/rooms/images/photos/9.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=100),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='service_bonus',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
