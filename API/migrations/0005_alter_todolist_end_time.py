# Generated by Django 4.0.5 on 2022-08-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_todolist_task_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='end_time',
            field=models.TimeField(default='12:00:00'),
        ),
    ]
