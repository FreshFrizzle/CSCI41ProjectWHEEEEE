from django.db import models

# Create your models here.
class Maintenance(models.Model):
    Maintenance_Num = models.AutoField(primary_key=True, max_length=5)


class Maintenance_Logs(models.Model):
    Maintenance_Num = models.ForeignKey(
        Maintenance,
        on_delete=models.CASCADE,
    )
    Train_ID = models.OneToOneField(
        Train,
        on_delete=models.CASCADE,
    )

class Maintenance_Task(models.Model):
    Maintenance_Num = models.ForeignKey(
        Maintenance,
        on_delete=models.CASCADE,
    )

    Task_ID = models.CharField(primary_key=True, max_length=5, default="00001")  

class Task(models.Model):
    Task_ID = models.ForeignKey(
        Maintenance_Task,
        on_delete=models.CASCADE,
    )
    Task_Name = models.CharField(primary_key=False, max_length=25, default="inspection")
    Crew_In_Charge = models.CharField(primary_key=False, max_length=25, default="J. Doe")
    Condition = models.CharField(primary_key=False, max_length=25, default="Horrible")





