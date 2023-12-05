from django.contrib import admin

from .models import MAINTENANCE, TASK, MAINTENANCE_LOGS, MAINTENANCE_TASK

class MaintenanceAdmin(admin.ModelAdmin):
    model = MAINTENANCE

class TaskAdmin(admin.ModelAdmin):
    model = TASK

class Maintenance_LogsAdmin(admin.ModelAdmin):
    model = MAINTENANCE_LOGS

class Maintenance_TaskAdmin(admin.ModelAdmin):
    model = MAINTENANCE_TASK

admin.site.register(MAINTENANCE, MaintenanceAdmin)
admin.site.register(TASK, TaskAdmin)
admin.site.register(MAINTENANCE_LOGS, Maintenance_LogsAdmin)
admin.site.register(MAINTENANCE_TASK, Maintenance_TaskAdmin)
