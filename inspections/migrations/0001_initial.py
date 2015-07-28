# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import phonenumber_field.modelfields
import inspections.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150727_2017'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.CharField(default=inspections.models.generate_referral_code, max_length=10, primary_key=True, serialize=False)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('technician', models.CharField(max_length=70)),
                ('comments', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='inspections')),
                ('vehicle', models.ForeignKey(to='vehicles.Vehicle', related_name='inspections')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, default='')),
                ('address', models.ForeignKey(to='core.Address')),
            ],
        ),
    ]
