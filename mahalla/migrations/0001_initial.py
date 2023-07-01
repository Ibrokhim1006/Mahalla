# Generated by Django 4.2.2 on 2023-06-29 09:16

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '0002_custumusers_position'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=250)),
                ('additional_information', ckeditor_uploader.fields.RichTextUploadingField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to=settings.AUTH_USER_MODEL)),
                ('id_categor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahalla.categoriya')),
                ('id_distirick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.district')),
                ('id_mahalla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.mahalla')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.region')),
                ('id_sektor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.sektor')),
                ('responsible_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskCategoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_user', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=250, null=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('date_line', models.DateField()),
                ('id_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahalla.people')),
                ('id_task_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahalla.taskcategoriya')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_responsible_employee', models.BooleanField(default=False)),
                ('is_task', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('id_task', models.ManyToManyField(to='mahalla.tasks')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
