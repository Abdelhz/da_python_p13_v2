from django.db import migrations

def copy_user_temp_to_user(apps, schema_editor):
    Profile = apps.get_model('profiles', 'Profile')
    for profile in Profile.objects.all():
        profile.user = profile.user_temp
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_user'),
    ]

    operations = [
        migrations.RunPython(copy_user_temp_to_user),
        migrations.RemoveField(
            model_name='profile',
            name='user_temp',
        ),
    ]