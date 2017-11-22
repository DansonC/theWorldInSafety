# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import management.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facility_name', models.CharField(max_length=256)),
                ('Facility_homepage', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['Facility_name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_name', models.CharField(max_length=128)),
                ('Video_snapshot', management.fields.VideoField(upload_to='video/%Y/%m')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('Video_checked', models.BooleanField(default=False)),
                ('Video_facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Facility')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]