# Generated by Django 3.0 on 2024-03-03 12:18

from django.db import migrations


address_mapping = {}

'''
def copy_addresses(apps, schema_editor):
    global address_mapping
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    Address = apps.get_model('lettings', 'Address')
    for old_address in OldAddress.objects.all():
        new_address = Address.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        address_mapping[old_address.id] = new_address


def colpy_lettings(apps, schema_editor):
    global address_mapping
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    Letting = apps.get_model('lettings', 'Letting')
    for old_letting in OldLetting.objects.all():
        Letting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address=address_mapping[old_etting.address.id],
        )
'''


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        #('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        #migrations.RunPython(copy_addresses),
        #migrations.RunPython(copy_lettings),
    ]