from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Django model representing an Address.

    This model has fields for the number, street, city, state,
    zip code, and country ISO code of the address.
    The number and zip code fields are positive integers with maximum values,
    the state and country ISO code fields
    are character fields with minimum lengths, and the street and city fields
    are character fields with maximum lengths.
    """

    class Meta:
        """
        Meta class for Address.

        This class defines the human-readable name for Address in its singular
        and plural forms.
        """
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return a string representation of the Address instance.

        The string is in the format 'number street'.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Django model representing a Letting.

    This model has a field for the title of the letting and a one-to-one
    relationship with the Address model.
    The address is deleted if the associated letting is deleted
    (`on_delete=models.CASCADE`).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the Letting instance as its string representation.
        """
        return self.title
