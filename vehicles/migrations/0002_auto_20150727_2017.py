# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('engine_type', models.CharField(serialize=False, max_length=30, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='body',
            field=models.ForeignKey(blank=True, null=True, to='vehicles.Body'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.ForeignKey(blank=True, null=True, to='vehicles.Trim'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, to='vehicles.Engine'),
        ),
    ]
