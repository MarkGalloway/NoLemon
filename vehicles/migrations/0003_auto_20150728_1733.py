# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150727_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colour',
            name='basic_colour',
        ),
        migrations.DeleteModel(
            name='BasicColour',
        ),
    ]
