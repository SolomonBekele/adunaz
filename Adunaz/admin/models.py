from django.db import models

# Create your models here.


class Image(models.Model):
    img_name = models.CharField(max_length=100)
    image_