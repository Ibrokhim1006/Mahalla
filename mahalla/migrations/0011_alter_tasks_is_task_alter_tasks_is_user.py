# Generated by Django 4.2.2 on 2023-07-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahalla', '0010_tasks_files_tasks_is_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='is_task',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='is_user',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]