# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('inspections', '0006_auto_20150728_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='group',
            field=models.OneToOneField(null=True, to='auth.Group', blank=True),
        ),
    ]
