# Generated by Django 3.1.2 on 2020-11-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0013_auto_20201101_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='shortName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
