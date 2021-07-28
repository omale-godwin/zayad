# Generated by Django 3.2.5 on 2021-07-20 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
