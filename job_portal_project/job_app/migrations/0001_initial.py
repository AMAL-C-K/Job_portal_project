# Generated by Django 5.1 on 2024-08-12 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('technical_skills', models.TextField()),
                ('softskills', models.TextField()),
                ('experience_category', models.CharField(max_length=150)),
                ('experience', models.CharField(max_length=250)),
                ('last_date', models.DateField()),
                ('salary', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('tags', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_app.category')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_app.roles')),
            ],
        ),
    ]
