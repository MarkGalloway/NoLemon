# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20150728_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='body',
            field=models.ForeignKey(null=True, to='vehicles.Body'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
