# Generated by Django 2.0.7 on 2019-10-27 07:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0030_auto_20191027_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 12, 35, 15, 823607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2293, 8, 10, 12, 35, 15, 824014, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 27, 12, 35, 15, 823951, tzinfo=utc), null=True),
        ),
    ]
