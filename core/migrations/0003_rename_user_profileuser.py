# Generated by Django 4.1.4 on 2023-01-07 10:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_remove_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='ProfileUser',
        ),
    ]
