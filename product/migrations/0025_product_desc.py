# Generated by Django 4.1.4 on 2023-01-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]