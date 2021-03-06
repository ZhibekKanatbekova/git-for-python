1# Generated by Django 3.1.3 on 2021-01-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
