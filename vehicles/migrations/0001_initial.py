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
                ('colour_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('body_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('colour_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('basic_colour', models.ForeignKey(related_name='basic_colour', to='vehicles.BasicColour')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('fuel_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('make_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('transmission_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('trim_type', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('body', models.ForeignKey(to='vehicles.Body')),
                ('colour', models.ForeignKey(to='vehicles.Colour')),
                ('fuel_type', models.ForeignKey(to='vehicles.Fuel')),
                ('make', models.ForeignKey(to='vehicles.Make')),
                ('model', models.ForeignKey(to='vehicles.Model')),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('transmission', models.ForeignKey(to='vehicles.Transmission')),
                ('trim', models.ForeignKey(to='vehicles.Trim')),
            ],
        ),
    ]
