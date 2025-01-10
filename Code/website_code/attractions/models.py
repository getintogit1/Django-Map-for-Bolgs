# attractions/models.py
from django.db import models



class Attraction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.CharField(max_length=200,default="")
    image = models.FileField(upload_to="attraction_images/", blank=True)
    address = models.CharField(max_length=150, default="")  # Provide a default value
    price = models.CharField(max_length=150,default="")
    link = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True)  # Add a SlugField to your model
