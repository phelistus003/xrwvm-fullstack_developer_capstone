# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

# <HINT> Create a Car Make model `class CarMake(models.Model)`:


class CarModel(models.Model):
    # Many-to-one relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="car_models")

    # Dealer ID referring to a dealer created in Cloudant database
    dealer_id = models.IntegerField()

    name = models.CharField(max_length=100)

    # Type choices matching standard conventions
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)

    # Year field strictly validated between 2015 and 2023 as specified by the hint
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
