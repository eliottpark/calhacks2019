# Generated by Django 2.0.7 on 2019-10-27 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0031_auto_20191027_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 13, 58, 48, 201820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2293, 8, 10, 13, 58, 48, 202059, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 27, 13, 58, 48, 202031, tzinfo=utc), null=True),
        ),
    ]
