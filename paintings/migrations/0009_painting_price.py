# Generated by Django 3.1.4 on 2020-12-10 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0008_auto_20201208_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]