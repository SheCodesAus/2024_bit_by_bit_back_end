# Generated by Django 5.0.3 on 2024-03-26 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_linkedin_customuser_slack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slack',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprocess',
            name='user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprocess',
            name='user_offboarding_task',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprocess',
            name='user_onboarding_task',
            field=models.TextField(blank=True, null=True),
        ),
    ]
