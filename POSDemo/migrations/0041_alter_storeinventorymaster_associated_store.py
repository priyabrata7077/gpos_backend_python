# Generated by Django 4.1.7 on 2023-03-30 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0040_alter_businessinventorymaster_associated_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinventorymaster',
            name='associated_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.storemaster'),
        ),
    ]