# Generated by Django 3.1.3 on 2021-01-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210125_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
