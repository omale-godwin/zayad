# Generated by Django 3.2.5 on 2021-07-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_l',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
