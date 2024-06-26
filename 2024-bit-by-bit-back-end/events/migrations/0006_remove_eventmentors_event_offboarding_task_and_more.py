# Generated by Django 5.0.3 on 2024-03-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_eventmentors_role_requested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmentors',
            name='event_offboarding_task',
        ),
        migrations.RemoveField(
            model_name='eventmentors',
            name='event_onboarding_task',
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_offboarding_task_feedbackreceived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_offboarding_task_invoicesent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_buildinginformation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_contract',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_createimgasset',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_googlecalendarinvite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_lmsinvite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_mentorbio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_reconfirmdates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventmentors',
            name='event_onboarding_task_slackinvite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='eventmentors',
            name='role_assigned',
            field=models.BooleanField(default=False),
        ),
    ]
