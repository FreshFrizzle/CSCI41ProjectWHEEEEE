from django.db import models
from datetime import date, time
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Train(models.Model):
    Train_ID = models.CharField(primary_key=True, max_length=6, default="000001")
    Model = models.CharField(primary_key=False, max_length=4, default="0001")
    Max_Speed = models.PositiveIntegerField(default=0)
    No_of_Seats = models.PositiveIntegerField(default=0)
    No_of_Toilets = models.PositiveIntegerField(default=0)
    Reclining_Seats = models.BooleanField(default=False)
    Folding_Tables = models.BooleanField(default=False)
    Disability_Access = models.BooleanField(default=False)
    Luggage_Storage = models.BooleanField(default=False)
    Vending_Machines = models.BooleanField(default=False)
    Food_Service = models.BooleanField(default=False)
    train_model_series = [
        ("S","S"),
        ("A","A"),
    ]
    Train_Type = models.CharField(primary_key=False, default="A", choices=train_model_series)

class Route(models.Model):
    Route_ID = models.CharField(primary_key=True, max_length=3, default="001")
    train_routes = [
        ("L","L"),
        ("I","I"),
    ]
    Route_Type = models.CharField(primary_key=False, default="L", choices=train_routes)

class S_Series(models.Model):
    S_Train_ID = models.OneToOneField(
        Train,
        on_delete=models.CASCADE
    )

class A_Series(models.Model):
    A_Train_ID = models.OneToOneField(
        Train,
        on_delete=models.CASCADE
    )

class Local(models.Model):
    L_Route_ID = models.OneToOneField(
        Route,
        on_delete=models.CASCADE
    )

class InterTown(models.Model):
    I_Route_ID = models.OneToOneField(
        Route,
        on_delete=models.CASCADE
    )