# Generated by Django 3.2.9 on 2021-12-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GW', '0002_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
