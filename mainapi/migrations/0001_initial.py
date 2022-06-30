# Generated by Django 4.0.4 on 2022-06-28 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('begins', models.TimeField(verbose_name=django.utils.timezone.now)),
                ('ends', models.TimeField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
