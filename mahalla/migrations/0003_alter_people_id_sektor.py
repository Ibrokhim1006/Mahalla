# Generated by Django 4.2.2 on 2023-06-29 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_custumusers_position'),
        ('mahalla', '0002_alter_people_id_mahalla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='id_sektor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authen.sektor'),
        ),
    ]