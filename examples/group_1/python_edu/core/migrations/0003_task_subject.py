# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171012_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Subject'),
            preserve_default=False,
        ),
    ]