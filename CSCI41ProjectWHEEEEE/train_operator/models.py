from django.db import models
from datetime import date, time
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
from django.db import models

# Create your models here.
class TRAIN_MODEL(models.Model):
    Model = models.CharField(primary_key=True, max_length=10, default="S-000")
    Max_Speed = models.CharField(primary_key=False, max_length=10, default="000 kph") 
    No_of_Seats = models.PositiveIntegerField(primary_key=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(999)])
    No_of_Toilets = models.PositiveIntegerField(primary_key=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    Reclining_Seats = models.BooleanField(primary_key=False, default=False)
    Folding_Tables = models.BooleanField(primary_key=False, default=False)
    Disability_Access = models.BooleanField(primary_key=False, default=False)
    Luggage_Storage = models.BooleanField(primary_key=False, default=False)
    Vending_Machines = models.BooleanField(primary_key=False,default=False)
    Food_Service = models.BooleanField(primary_key=False,default=False)
    Train_Type = models.CharField(primary_key=False,max_length=2, default="A")

class TRAIN(models.Model):
    Train_ID = models.CharField(primary_key=True, max_length=6, default="000001")
    Model = models.OneToOneField(
        TRAIN_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return '{}'.format(self.pk)

class ROUTE(models.Model):
    Route_ID = models.CharField(primary_key=True, max_length=3, default="001")
    Train_Type = models.CharField(primary_key=False,max_length=2, default="L") 

    def get_absolute_url(self):
        return '{}'.format(self.pk)

class S_SERIES(models.Model):
    S_Train_ID = models.CharField(primary_key=True, max_length=10, default="S-001")

class A_SERIES(models.Model):
    A_Train_ID = models.CharField(primary_key=True, max_length=10, default="A-001")

class LOCAL(models.Model):
    L_Route_ID = models.CharField(primary_key=True, max_length=10, default="L-001")

class INTER_TOWN(models.Model):
    I_Route_ID = models.CharField(primary_key=True, max_length=10, default="I-001")

class S_SERIES_ROUTING(models.Model):
    S_Train_ID = models.ForeignKey(
        S_SERIES,
        on_delete=models.CASCADE,
        ) 
    I_Route_ID = models.ForeignKey(
        INTER_TOWN,
        on_delete=models.CASCADE,
        ) 

class A_SERIES_ROUTING(models.Model):
    A_Train_ID = models.ForeignKey(
        A_SERIES,
        on_delete=models.CASCADE,
        ) 
    L_Route_ID = models.ForeignKey(
        LOCAL,
        on_delete=models.CASCADE,
        ) 