from django.db import models


# Create your models here.

unit_choice = [
    ('Hourly', 'Hourly'),
    ('Daily', 'Daily'),
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
]


class HouseRent(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=unit_choice)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to="house_image")
    description = models.TextField(max_length=500)


class CarRent(models.Model):
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=unit_choice)
    image = models.ImageField(upload_to="car_image")
    description = models.TextField(max_length=500)


class WareHouseRent(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=4)
    location = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=unit_choice)
    image = models.ImageField(upload_to="house_image")
    description = models.TextField(max_length=500)
