# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0012_auto_20150730_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='image_back',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='image_dash',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='image_drivers_side',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='image_front',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='image_interior',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='image_passengers_side',
            field=ajaximage.fields.AjaxImageField(null=True),
        ),
    ]
