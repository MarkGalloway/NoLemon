# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
        ('advertisements', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='address',
            field=models.ForeignKey(related_name='advertisements', to='core.Address'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='article',
            field=models.ForeignKey(related_name='advertisements', to='vehicles.Vehicle'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ManyToManyField(to='advertisements.Image', through='advertisements.AdvertisementImage', related_name='advertisements'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='seller',
            field=models.ForeignKey(related_name='advertisements', to=settings.AUTH_USER_MODEL),
        ),
    ]
