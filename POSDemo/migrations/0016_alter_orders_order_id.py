# Generated by Django 4.1.7 on 2023-03-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0015_day_wise_employee_management_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.IntegerField(unique=True),
        ),
    ]