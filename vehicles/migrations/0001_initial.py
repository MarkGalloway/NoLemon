# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicColour',
            fields=[
                ('colour_name', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('body_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('colour_name', models.CharField(primary_key=True, max_length=30, serialize=False)),
                ('basic_colour', models.ForeignKey(related_name='colours', to='vehicles.BasicColour')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('fuel_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('make_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
                ('make', models.ForeignKey(related_name='models', to='vehicles.Make')),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('transmission_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('trim_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('mileage', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('body', models.ForeignKey(to='vehicles.Body')),
                ('car_model', models.ForeignKey(to='vehicles.Model')),
                ('colour', models.ForeignKey(to='vehicles.Colour')),
                ('fuel_type', models.ForeignKey(to='vehicles.Fuel')),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('transmission', models.ForeignKey(to='vehicles.Transmission')),
                ('trim', models.ForeignKey(to='vehicles.Trim')),
            ],
        ),
    ]
