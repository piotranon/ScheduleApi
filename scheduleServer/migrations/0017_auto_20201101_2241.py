# Generated by Django 3.1.2 on 2020-11-01 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0016_auto_20201101_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldofstudy',
            old_name='specialization',
            new_name='specializations',
        ),
    ]
