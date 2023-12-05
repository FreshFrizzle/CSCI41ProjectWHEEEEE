from django.db import models
from datetime import date, time
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models import Sum
from train_operator.models import TRAIN, ROUTE

# Create your models here.
class CUSTOMER(models.Model):
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
    Gender = models.CharField(max_length=25, primary_key=False, choices=genderChoices, default="Male")


class STATION(models.Model):
    Station_ID = models.CharField(primary_key=True, max_length=25, default="AAA")
    Location = models.CharField(primary_key=False, max_length=25, default=("BD", "Beaver's Dam"))


class TICKET(models.Model):
    Ticket_number = models.CharField(primary_key=True, max_length=4, default="0001")
    Customer_ID = models.OneToOneField(
        CUSTOMER,
        on_delete=models.CASCADE,
    )
    Date = models.DateField(auto_now=False,auto_now_add=False,default=date(1970,1,1))

    @property
    def Total_Cost(self):
        # gather all trips connected to this ticket 
        tripsWithTicket = TICKET.TRIP_LOGS_set.all()

        trips_total_cost = tripsWithTicket.objects.all().aggregate(Sum('Cost'))['Cost']
        return trips_total_cost

class TRIP(models.Model):
    Trip_ID = models.CharField(primary_key=True, max_length=5, default="00001")
    Train_ID = models.ForeignKey(
        TRAIN,
        on_delete=models.CASCADE,
        ) 
    Station_ID = models.ForeignKey(
        STATION,
        on_delete=models.CASCADE,
    )
    Route_ID = models.ForeignKey(
        ROUTE,
        on_delete=models.CASCADE,
    )
    Origin = models.CharField(primary_key=False, max_length=25, default="Allies’ Enclave")
    Destination = models.CharField(primary_key=False, max_length=25, default="Dancing Lawn")
    Departure = models.TimeField(auto_now=False, auto_now_add=False, default=time(0,0))
    Arrival = models.TimeField(auto_now=False, auto_now_add=False, default=time(0,0))
    Cost = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])

    @property
    def Duration(self):
        return self.Arrival - self.Departure
        

class TRIP_LOGS(models.Model):
    Trip_ID = models.ForeignKey(
        TRIP,
        on_delete=models.CASCADE,
    )

    Ticket_Num = models.ForeignKey(
        TICKET,
        on_delete=models.CASCADE,
    )
    pass

    