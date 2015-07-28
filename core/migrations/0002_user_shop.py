# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_auto_20150727_2149'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shop',
            field=models.ForeignKey(related_name='users', help_text='Used if a user is a mechanic to designate their shop.', to='inspections.Shop', null=True, blank=True, verbose_name='Technician Shop'),
        ),
    ]
