# Generated by Django 2.1.5 on 2019-01-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181117_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='defeat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='victory',
            field=models.IntegerField(default=0),
        ),
    ]
