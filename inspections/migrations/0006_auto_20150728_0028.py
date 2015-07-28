# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0005_auto_20150727_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=15, default='', blank=True, validators=[django.core.validators.RegexValidator(message='Phone number should include 3 digit area code, and 7 digit number.', regex=re.compile("\n    (\\d{3})     # area code is 3 digits (e.g. '800')\n    \\D*         # optional separator is any number of non-digits\n    (\\d{3})     # trunk is 3 digits (e.g. '555')\n    \\D*         # optional separator\n    (\\d{4})     # rest of number is 4 digits (e.g. '1212')\n    \\D*         # optional separator\n    (\\d*)       # extension is optional and can be any number of digits\n    $           # end of string\n    ", 96))]),
        ),
    ]
