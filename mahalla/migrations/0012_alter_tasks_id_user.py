# Generated by Django 4.2.2 on 2023-07-01 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mahalla', '0011_alter_tasks_is_task_alter_tasks_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
