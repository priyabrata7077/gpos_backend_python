# Generated by Django 4.1.7 on 2023-04-19 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0113_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roles',
            old_name='permisssions',
            new_name='permissions',
        ),
    ]