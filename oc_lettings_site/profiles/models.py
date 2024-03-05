from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Django model that represents a user profile.

    Each user profile is linked to a single Django User instance.
    A user profile has a 'favorite_city' attribute
    which is a string that can be left blank.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        On user deletion, the profile is also deleted.
        favorite_city (CharField): A character field that stores the user's
        favorite city. Can be left blank.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Profile model.

        The string representation is the username of the linked User instance.

        Returns:
            str: The username of the linked User instance.
        """
        return self.user.username
