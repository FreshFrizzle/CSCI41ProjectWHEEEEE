TASK.objects.raw("SELECT * FROM train_maintenance_task WHERE Task_id = '059'")

TASK.objects.raw("SELECT * FROM train_maintenance_task WHERE Task_Name = 'Cleaning Toilets'")

TRAIN_MODEL.objects.raw("SELECT * FROM train_operator_train_model WHERE Folding_Tables = TRUE")

TRAIN_MODEL.objects.raw("SELECT * FROM train_operator_train_model WHERE Disability_Access = FALSE")

MAINTENANCE.objects.raw("SELECT * FROM train_maintenance_maintenance WHERE Maintenance_Num != '0991'")