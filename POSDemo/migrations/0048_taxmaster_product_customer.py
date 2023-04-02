# Generated by Django 4.1.7 on 2023-04-01 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0047_ownerdetails_remove_brand_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('MRP', models.CharField(max_length=20)),
                ('purchase_rate', models.CharField(max_length=20)),
                ('sale_rate', models.CharField(max_length=20)),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='POSDemo.taxmaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='POSDemo.storemaster')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10, unique=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to='POSDemo.storemaster')),
            ],
        ),
    ]
