# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0008_auto_20150728_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection',
            old_name='user',
            new_name='customer',
        ),
    ]
