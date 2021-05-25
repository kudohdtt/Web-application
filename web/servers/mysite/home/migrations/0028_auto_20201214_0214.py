# Generated by Django 3.1.3 on 2020-12-13 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201209_1847'),
        ('home', '0027_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField()),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
                ('roomtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.roomtype')),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]