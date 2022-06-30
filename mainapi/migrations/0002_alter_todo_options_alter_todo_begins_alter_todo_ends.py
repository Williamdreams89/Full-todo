# Generated by Django 4.0.5 on 2022-06-29 23:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'a todo', 'verbose_name_plural': 'Todolist'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='begins',
            field=models.TimeField(verbose_name=datetime.datetime(2022, 6, 29, 23, 42, 32, 344653, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='ends',
            field=models.TimeField(verbose_name=datetime.datetime(2022, 6, 29, 23, 42, 32, 344653, tzinfo=utc)),
        ),
    ]
