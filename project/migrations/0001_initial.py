# Generated by Django 5.1.3 on 2024-11-29 10:43

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
                ('name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Updateimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('client', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=250, null=True)),
                ('image', models.CharField(max_length=250)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='project.category')),
            ],
            options={
                'verbose_name_plural': 'project',
                'ordering': ('title',),
            },
        ),
    ]
