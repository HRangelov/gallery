# Generated by Django 3.1.4 on 2020-12-02 13:25

from django.db import migrations, models
import django.db.models.deletion
import paintings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Realism', 'Realism'), ('Photorealism', 'Photorealism'), ('Impressionism', 'Impressionism'), ('Abstract', 'Abstract'), ('Surrealism', 'Surrealism'), ('Pop', 'Pop'), ('Unknown', 'Unknown')], default='Unknown', max_length=13)),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=12)),
                ('artist', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='paintings', validators=[paintings.models.is_jpg_or_jpeg_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=2)),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paintings.painting')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paintings.painting')),
            ],
        ),
    ]
