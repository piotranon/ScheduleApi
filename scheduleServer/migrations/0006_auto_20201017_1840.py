# Generated by Django 3.1.2 on 2020-10-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0005_auto_20201017_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='building',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]