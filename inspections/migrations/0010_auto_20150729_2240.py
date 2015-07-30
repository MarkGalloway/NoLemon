# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import inspections.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspections', '0009_auto_20150728_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionCode',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, default=inspections.models.generate_referral_code, primary_key=True)),
                ('is_redeemed', models.BooleanField(verbose_name='Redeemed', default=False)),
                ('redeemed_on', models.DateField(verbose_name='Redeemed', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='inspection_codes')),
            ],
        ),
        migrations.AlterField(
            model_name='inspection',
            name='id',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='license_light',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Not-Applicable'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='trunk_light',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Not-Applicable'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='windshield',
            field=inspections.models.RadioSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
    ]
