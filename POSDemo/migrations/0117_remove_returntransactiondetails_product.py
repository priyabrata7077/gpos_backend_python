# Generated by Django 4.1.7 on 2023-04-24 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0116_remove_returntransactiondetails_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returntransactiondetails',
            name='product',
        ),
    ]