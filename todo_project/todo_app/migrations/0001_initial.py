# Generated by Django 3.1.1 on 2020-10-09 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('finished', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
