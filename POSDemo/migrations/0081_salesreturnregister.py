# Generated by Django 4.1.7 on 2023-04-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0080_employeeattendance_returnsalespending_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReturnRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100, null=True)),
                ('product', models.JSONField(null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=100)),
                ('quantity_returned', models.CharField(max_length=100)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.business')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.employeemaster')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesreturn', to='POSDemo.storemaster')),
            ],
        ),
    ]
