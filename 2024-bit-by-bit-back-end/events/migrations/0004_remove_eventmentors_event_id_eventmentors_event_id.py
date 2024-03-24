# Generated by Django 5.0.3 on 2024-03-23 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_eventmentors_event_id_eventmentors_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmentors',
            name='event_id',
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.events'),
            preserve_default=False,
        ),
    ]