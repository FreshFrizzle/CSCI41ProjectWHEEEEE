from django.db import models
from datetime import date, time
from train_operator.models import TRAIN

# Create your models here.
class MAINTENANCE(models.Model):
    maintenance_num = models.CharField(primary_key=True, max_length=4, default="0001")
    pass

#for maintenance in MAINTENANCE.objects.raw("SELECT * FROM train_maintenance_maintenance")

class TASK(models.Model):
    Task_id = models.CharField(primary_key=True, max_length=3, default="001")
    Task_name = models.CharField(primary_key=False, max_length=25, default="Checking Train Brakes")
    Date = models.DateField(auto_now=False, auto_now_add=False, default=date(1970,1,1))
    Crew_in_charge = models.CharField(primary_key=False, max_length=25, default="J. Doe")
    Condition = models.CharField(primary_key=False, max_length=25, default="Good")

#for task in TASK.objects.raw("SELECT * FROM train_maintenance_task")


class MAINTENANCE_TASK(models.Model):
    maintenance_num = models.ForeignKey(
        MAINTENANCE,
        on_delete=models.CASCADE,
    )
    
    task_id = models.ForeignKey(
        TASK, 
        on_delete=models.CASCADE,
    )


#for maintenance_task in MAINTENANCE_TASK.objects.raw("SELECT * FROM train_maintenance_maintenance_task") 

class MAINTENANCE_LOGS(models.Model):
    maintenance_num = models.ForeignKey(
        MAINTENANCE, on_delete=models.CASCADE
        )
    train_id = models.ForeignKey(
        TRAIN, on_delete=models.CASCADE
        )
    pass

#for maintenance_logs in MAINTENANCE_LOGS.objects.raw("SELECT * FROM train_maintenance_maintenance_logs")

