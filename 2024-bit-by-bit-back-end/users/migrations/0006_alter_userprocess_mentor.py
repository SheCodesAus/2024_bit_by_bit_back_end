# Generated by Django 5.0.3 on 2024-03-30 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_userprocess_user_offboarding_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprocess',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onboarded_mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
