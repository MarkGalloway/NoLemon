# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
from django.conf import settings
import django.utils.timezone


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
            name='BasicColourAuditLogEntry',
            fields=[
                ('colour_name', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_basiccolour_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('body_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='BodyAuditLogEntry',
            fields=[
                ('body_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_body_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('colour_name', models.CharField(primary_key=True, max_length=30, serialize=False)),
                ('basic_colour', models.ForeignKey(to='vehicles.BasicColour', related_name='basic_colour')),
            ],
        ),
        migrations.CreateModel(
            name='ColourAuditLogEntry',
            fields=[
                ('colour_name', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_colour_audit_log_entry')),
                ('basic_colour', models.ForeignKey(to='vehicles.BasicColour', related_name='_auditlog_basic_colour')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('fuel_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FuelAuditLogEntry',
            fields=[
                ('fuel_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_fuel_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('make_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MakeAuditLogEntry',
            fields=[
                ('make_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_make_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ModelAuditLogEntry',
            fields=[
                ('model_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_model_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('transmission_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionAuditLogEntry',
            fields=[
                ('transmission_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_transmission_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('trim_type', models.CharField(primary_key=True, max_length=30, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrimAuditLogEntry',
            fields=[
                ('trim_type', models.CharField(max_length=30, db_index=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('action_type', models.CharField(editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='_trim_audit_log_entry')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=250, blank=True)),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('body', models.ForeignKey(to='vehicles.Body')),
                ('colour', models.ForeignKey(to='vehicles.Colour')),
                ('fuel_type', models.ForeignKey(to='vehicles.Fuel')),
                ('make', models.ForeignKey(to='vehicles.Make')),
                ('model', models.ForeignKey(to='vehicles.Model')),
                ('transmission', models.ForeignKey(to='vehicles.Transmission')),
                ('trim', models.ForeignKey(to='vehicles.Trim')),
            ],
        ),
    ]
