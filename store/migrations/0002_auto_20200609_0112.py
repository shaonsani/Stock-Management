# Generated by Django 3.0.6 on 2020-06-09 01:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 1, 12, 20, 823121, tzinfo=utc)),
        ),
    ]
