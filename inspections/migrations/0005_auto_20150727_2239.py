# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0004_auto_20150727_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='backup_lights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='dome_lights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='exterior_condition',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='fog_lights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='hazard_lights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='headlights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='license_light',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='mirrors',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='signal_lights',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='trunk_light',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='windows',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='windshield',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='wipers',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Fair'), (3, 'Poor')], default=3),
        ),
    ]
