# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shop',
        ),
    ]
