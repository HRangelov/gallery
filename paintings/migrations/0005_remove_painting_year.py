# Generated by Django 3.1.4 on 2020-12-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0004_auto_20201204_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painting',
            name='year',
        ),
    ]
