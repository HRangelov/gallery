# Generated by Django 3.1.4 on 2020-12-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0002_painting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='year',
            field=models.CharField(),
        ),
    ]
