# Generated by Django 3.0 on 2024-03-03 12:18

from django.db import migrations


'''
def copy_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')
    for old_profile in OldProfile.objects.all():
        Profile.objects.create(
            id=old_profile.id,
            user_temp=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )
'''
class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        #('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        #migrations.RunPython(copy_profiles),
    ]
