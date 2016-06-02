# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-01 21:10
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.migrations.operations.special
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# events.migrations.0004_add_keynoteevent
# events.migrations.0005_add_proposedtalkevent

class Migration(migrations.Migration):

    replaces = [
        ('events', '0004_add_keynoteevent'),
        ('events', '0005_add_proposedtalkevent'),
        ('events', '0006_add_customevent'),
        ('events', '0007_schedule'),
    ]

    dependencies = [
        ('events', '0003_time_location_in_sponsoredevent'),
        ('proposals', '0027_auto_20160426_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeynoteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('2-all', 'All rooms'), ('3-r012', 'R0, R1, R2'), ('4-r0', 'R0'), ('5-r1', 'R1'), ('6-r2', 'R2'), ('1-r3', 'R3')], db_index=True, max_length=6, null=True, verbose_name='location')),
                ('speaker_name', models.CharField(max_length=100, verbose_name='speaker name')),
                ('slug', models.SlugField(help_text="This is used to link to the speaker's introduction on the Keynote page, e.g. 'liang2' will link to '/None/events/keynotes/#keynote-speaker-liang2'.", verbose_name='slug')),
                ('begin_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='begined_keynoteevent_set', to='events.Time', verbose_name='begin time')),
                ('end_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ended_keynoteevent_set', to='events.Time', verbose_name='end time')),
            ],
            options={
                'verbose_name': 'keynote event',
                'verbose_name_plural': 'keynote events',
            },
        ),
        migrations.CreateModel(
            name='ProposedTalkEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('2-all', 'All rooms'), ('3-r012', 'R0, R1, R2'), ('4-r0', 'R0'), ('5-r1', 'R1'), ('6-r2', 'R2'), ('1-r3', 'R3')], db_index=True, max_length=6, null=True, verbose_name='location')),
                ('begin_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='begined_proposedtalkevent_set', to='events.Time', verbose_name='begin time')),
                ('end_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ended_proposedtalkevent_set', to='events.Time', verbose_name='end time')),
                ('proposal', core.models.BigForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.TalkProposal', verbose_name='proposal')),
            ],
            options={
                'verbose_name': 'talk event',
                'verbose_name_plural': 'talk events',
            },
        ),
        migrations.CreateModel(
            name='CustomEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('2-all', 'All rooms'), ('3-r012', 'R0, R1, R2'), ('4-r0', 'R0'), ('5-r1', 'R1'), ('6-r2', 'R2'), ('1-r3', 'R3')], db_index=True, max_length=6, null=True, verbose_name='location')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('begin_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='begined_customevent_set', to='events.Time', verbose_name='begin time')),
                ('end_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ended_customevent_set', to='events.Time', verbose_name='end time')),
            ],
            options={
                'verbose_name': 'custom event',
                'verbose_name_plural': 'custom events',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField(verbose_name='HTML')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
                'get_latest_by': 'created_at',
            },
        ),
    ]