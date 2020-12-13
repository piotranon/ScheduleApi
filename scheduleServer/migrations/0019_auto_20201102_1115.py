# Generated by Django 3.1.2 on 2020-11-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0018_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldofstudy',
            name='groups',
            field=models.ManyToManyField(related_name='field1', to='scheduleServer.Groups'),
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='laboratories',
            field=models.ManyToManyField(related_name='field2', to='scheduleServer.Groups'),
        ),
    ]
