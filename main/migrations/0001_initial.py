# Generated by Django 3.1.3 on 2021-01-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favourite', models.BooleanField(default=False)),
            ]
        ),
    ]
