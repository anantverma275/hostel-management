# Generated by Django 3.1.1 on 2020-09-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200908_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='room_no',
            field=models.IntegerField(null=True),
        ),
    ]