# Generated by Django 3.1.2 on 2020-11-12 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleServer', '0019_auto_20201102_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduleServer.specialization'),
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='fielf_of_study',
        ),
        migrations.AddField(
            model_name='lecture',
            name='fielf_of_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduleServer.fieldofstudy'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecture_group', to='scheduleServer.groups'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='laboratories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecture_laboratories', to='scheduleServer.groups'),
        ),
    ]