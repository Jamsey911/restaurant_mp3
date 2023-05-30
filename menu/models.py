# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Food and Drinks type so all food and drinks can be categorised
FOOD_TYPE = ((0, "Starters"), (1, "Mains"), (2, "Desserts"), (3, "New"))
DRINK_TYPE = (
    (0, "White Wine"),
    (1, "Red Wine"),
    (2, "Rose Wine"),
    (3, "Prosecco"),
    (4, "Beers"),
    (5, "Cocktails"),
    (6, "Spirits"),
    (7, "New"),
)


# Model for Food items


class FoodItem(models.Model):
    """
    a class for the food item model, contains
    starters, mains and dessert foods
    """

    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    food_type = models.IntegerField(choices=FOOD_TYPE, default=3)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-food_type"]

    def __str__(self):
        return self.food_name


# Model for Drink items


class DrinkItem(models.Model):
    """
    a class for the drink item model, contains
    wines, beers and cocktails
    """

    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    drink_type = models.IntegerField(choices=DRINK_TYPE, default=3)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-available"]

    def __str__(self):
        return self.drink_name
