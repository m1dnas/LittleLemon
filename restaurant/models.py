from django.db import models

class Booking(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.IntegerField()
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()