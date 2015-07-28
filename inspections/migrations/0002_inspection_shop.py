# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='shop',
            field=models.ForeignKey(default='', to='inspections.Shop', verbose_name='Mechanic Shop', help_text='Used if a user is a mechanic to designate their shop.'),
            preserve_default=False,
        ),
    ]
