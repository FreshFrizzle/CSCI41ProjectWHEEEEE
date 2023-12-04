from django.db import models

# Create your models here.
class MAINTENANCE(models.Model):
    maintenance_num = models.CharField(max_length=4)
    pass

for maintenance in Maintenance.objects.raw("SELECT * FROM train_maintenance_maintenance")

class MAINTENANCE_TASK(models.Model):
    maintenance_num = models.ForeignKey(Location, on_delete=models.CASCADE)
	task_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    pass

for maintenance_task in Maintenance_Task.objects.raw("SELECT * FROM train_maintenance_maintenance_task") 

class MAINTENANCE_LOGS(models.Model):
    maintenance_num = models.ForeignKey(Location, on_delete=models.CASCADE)
    train_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    pass

for maintenance_logs in Maintenance_Logs.objects.raw("SELECT * FROM train_maintenance_maintenance_logs")

class TASK(models.Model):
    task_id = 
    task_name = 
    date =
    crew_in_charge = 
    condition = 
    pass

for task in Task.objects.raw("SELECT * FROM train_maintenance_task")
