# Generated by Django 4.1.7 on 2023-03-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0041_alter_storeinventorymaster_associated_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeinventorymaster',
            name='store_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='POSDemo.owner'),
        ),
    ]
