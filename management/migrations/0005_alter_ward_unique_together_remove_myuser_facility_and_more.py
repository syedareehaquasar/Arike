# Generated by Django 4.0.3 on 2022-03-06 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_myuser_groups_alter_myuser_user_permissions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ward',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='UserProfile',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='UserProfile',
            name='ward',
        ),
        migrations.AddField(
            model_name='facility',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ward',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
