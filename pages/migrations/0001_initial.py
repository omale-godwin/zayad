# Generated by Django 3.2.5 on 2021-07-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('galary', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]