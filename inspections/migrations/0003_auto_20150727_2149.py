# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0002_inspection_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='shop',
            field=models.ForeignKey(related_name='inspections', to='inspections.Shop', verbose_name='Technician Shop'),
        ),
    ]
