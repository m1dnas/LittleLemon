from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'