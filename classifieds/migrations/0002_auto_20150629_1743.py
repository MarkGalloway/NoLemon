# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
        ('classifieds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classified',
            name='address',
            field=models.ForeignKey(related_name='classifieds', to='core.Address'),
        ),
        migrations.AddField(
            model_name='classified',
            name='image',
            field=models.ManyToManyField(through='classifieds.ClassifiedImage', related_name='classifieds', to='classifieds.Image'),
        ),
        migrations.AddField(
            model_name='classified',
            name='seller',
            field=models.ForeignKey(related_name='classifieds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classified',
            name='vehicle',
            field=models.ForeignKey(related_name='classifieds', to='vehicles.Vehicle'),
        ),
    ]
