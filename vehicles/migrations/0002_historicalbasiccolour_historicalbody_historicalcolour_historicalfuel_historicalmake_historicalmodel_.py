# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBasicColour',
            fields=[
                ('colour_name', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical basic colour',
            },
        ),
        migrations.CreateModel(
            name='HistoricalBody',
            fields=[
                ('body_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical body',
            },
        ),
        migrations.CreateModel(
            name='HistoricalColour',
            fields=[
                ('colour_name', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('basic_colour', models.ForeignKey(to='vehicles.BasicColour', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical colour',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFuel',
            fields=[
                ('fuel_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical fuel',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMake',
            fields=[
                ('make_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical make',
            },
        ),
        migrations.CreateModel(
            name='HistoricalModel',
            fields=[
                ('model_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical model',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTransmission',
            fields=[
                ('transmission_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical transmission',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTrim',
            fields=[
                ('trim_type', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical trim',
            },
        ),
        migrations.CreateModel(
            name='HistoricalVehicle',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_index=True, blank=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('body', models.ForeignKey(to='vehicles.Body', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('colour', models.ForeignKey(to='vehicles.Colour', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('fuel_type', models.ForeignKey(to='vehicles.Fuel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')),
                ('make', models.ForeignKey(to='vehicles.Make', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('model', models.ForeignKey(to='vehicles.Model', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('transmission', models.ForeignKey(to='vehicles.Transmission', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
                ('trim', models.ForeignKey(to='vehicles.Trim', null=True, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, related_name='+', db_constraint=False)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical vehicle',
            },
        ),
    ]
