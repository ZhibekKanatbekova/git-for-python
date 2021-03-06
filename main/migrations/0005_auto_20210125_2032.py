# Generated by Django 3.1.3 on 2021-01-25 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210123_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='some string', max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='some string'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='some string', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=170),
        ),
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(default='some string', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='some string', max_length=100),
        ),
    ]
