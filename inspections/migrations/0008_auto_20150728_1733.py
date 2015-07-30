# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspections.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0007_shop_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, editable=False, default=inspections.models.generate_referral_code, max_length=10),
        ),
    ]
