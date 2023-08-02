# Generated by Django 4.1.7 on 2023-08-02 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0005_storestock_sales_store_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='POSDemo.business')),
                ('cat_parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='POSDemo.category')),
            ],
        ),
    ]
