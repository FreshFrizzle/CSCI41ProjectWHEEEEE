from django.db import models
from datetime import date, time
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Customer(models.Model):
    Customer_ID = models.CharField(primary_key=True, max_length=4, default="0001")
    Last_Name = models.CharField(primary_key=False, max_length=25, default="Doe")
    Given_Name = models.CharField(primary_key=False, max_length=25, default="John")
    Middle_Initial = models.CharField(primary_key=False, max_length=2, null=True, default="A", blank=True)
    Birth_Date = models.DateField(auto_now=False, auto_now_add=False, default=date(1970,1,1))
    genderChoices = [
        ("Male","Male"),
        ("Female","Female"),
        ("Non-binary","Non-binary"),
        ("Other","Other")
    ]
    Gender = models.CharField(primary_key=False, choices=genderChoices, default="Male")

class Ticket(models.Model):
    Ticket_number = models.CharField(primary_key=True, max_length=4, default="0001")
    Date = models.DateField(auto_now=False,auto_now_add=False,default=date(1970,1,1))
    Total_Cost = models.IntegerField(default=0)

class Trip(models.Model):
    Trip_Num = models.CharField(primary_key=True, max_length=5, default="00001")
    Train_Num = models.ManyToManyField(Train) #will fix later in the train models
    Origin = models.CharField(primary_key=False, max_length=25, default="Allies’ Enclave")
    Destination = models.CharField(primary_key=False, max_length=25, default="Cauldron Pool")
    Departure = models.TimeField(auto_now=False, auto_now_add=False, default=time(0,0))
    Arrival = models.TimeField(auto_now=False, auto_now_add=False, default=time(0,0))
    Duration = Arrival-Departure #will ask Yso about this
    Cost = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])

class Station(models.Model):
    Station_ID = models.CharField(primary_key=True, max_length=25, default="AAA")
    station_locations = [
        ("BD", "Beaver's Dam"),
        ("TLP", "The Lamp Post"),
        ("AE", "Allies' Enclave"),
        ("TW", "The Wardrobe"),
        ("MT", "Mr. Tumms"),
        ("AC", "Aslan's Camp"),
        ("WC", "Witch's Camp"),
        ("CP", "Cauldron Pool"),
        ("TST", "The Stone Table"),
        ("FC", "Father Christmas"),
        ("DL", "Dancing Lawn"),
        ("CT", "Cherry Tree"),
        ("A", "Anvard"),
    ]
    Location = models.CharField(primary_key=False, max_length=25, choices=station_locations, default=("BD", "Beaver's Dam"))
    