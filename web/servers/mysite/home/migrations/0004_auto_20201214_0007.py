# Generated by Django 3.1.3 on 2020-12-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_order_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=1000),
        ),
    ]