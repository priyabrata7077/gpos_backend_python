# Generated by Django 4.1.7 on 2023-04-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0072_salesregister_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='adhaar',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
