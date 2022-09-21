from django.db import models

# Create your models here.


class Land(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to="land_image")
    description = models.TextField(max_length=500)


class House(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=150)
    facing = models.CharField(max_length=20, choices=(
        ("North", "North"), ("East", "East"), ("West", "West"), ("South", "South")))
    image = models.ImageField(upload_to="house_image")
    description = models.TextField(max_length=500)


class Car(models.Model):
    car_condition = (
        ('New', "New"),
        ('Used', "Used"),
        ('Slightly used', "Slightly used"),
        ('Used in foreign country', "Used in foreign country"),
    )
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=30, choices=car_condition)
    image = models.ImageField(upload_to="car_image")
    description = models.TextField(max_length=500)


