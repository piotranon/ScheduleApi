# Generated by Django 3.1.2 on 2020-10-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0004_auto_20201017_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='weeks',
            field=models.CharField(choices=[('all', 'all'), ('1/3', '1/3'), ('2/4', '2/4')], max_length=100, null=True),
        ),
    ]