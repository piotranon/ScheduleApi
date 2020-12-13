# Generated by Django 3.1.2 on 2020-10-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldofstudy',
            name='lectures',
            field=models.ManyToManyField(to='scheduleServer.Lecture'),
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='semester',
            field=models.IntegerField(blank=True, choices=[(1, '1year 1semester'), (2, '1year 2semester'), (3, '2year 1semester'), (4, '2year 2semester'), (5, '3year 1semester'), (6, '3year 2semester'), (7, '4year 1semester')], null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='weekday',
            field=models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True),
        ),
    ]