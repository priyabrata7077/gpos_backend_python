# Generated by Django 4.1.7 on 2023-03-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0024_remove_business_business_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
