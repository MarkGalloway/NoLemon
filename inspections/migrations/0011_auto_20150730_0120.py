# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import inspections.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0010_auto_20150729_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='backup_lights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='inspections', null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='dome_lights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='exterior_condition',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='exterior_notes',
            field=models.TextField(default='', null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='fog_lights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='hazard_lights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='headlights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='license_light',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(0, 'Not-Applicable'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='mirrors',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='shop',
            field=models.ForeignKey(related_name='inspections', to='inspections.Shop', verbose_name='Technician Shop', null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='signal_lights',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='technician',
            field=models.CharField(null=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='trunk_light',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(0, 'Not-Applicable'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='vehicle',
            field=models.ForeignKey(to='vehicles.Vehicle', related_name='inspections', null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='windows',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='windshield',
            field=inspections.models.RadioSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='wipers',
            field=models.PositiveSmallIntegerField(default=3, null=True, choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')]),
        ),
        migrations.AlterField(
            model_name='inspectioncode',
            name='redeemed_on',
            field=models.DateField(null=True, verbose_name='Redeemed On'),
        ),
    ]
