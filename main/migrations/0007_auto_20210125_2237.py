# Generated by Django 3.1.3 on 2021-01-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_book_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
