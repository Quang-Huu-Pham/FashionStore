# Generated by Django 4.1.4 on 2023-01-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profileuser_avatar_alter_profileuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/user'),
        ),
    ]
