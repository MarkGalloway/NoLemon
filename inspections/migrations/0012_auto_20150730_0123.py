# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0011_auto_20150730_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='inspections'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='shop',
            field=models.ForeignKey(verbose_name='Technician Shop', related_name='inspections', to='inspections.Shop'),
        ),
    ]
