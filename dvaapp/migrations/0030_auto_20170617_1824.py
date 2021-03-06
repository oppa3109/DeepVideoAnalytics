# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0029_auto_20170617_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='end_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='segment_end', to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='segment',
            name='start_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='segment_start', to='dvaapp.Frame'),
        ),
    ]
