# Generated by Django 5.0.2 on 2024-03-04 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0003_alter_address_id_alter_letting_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
    ]
