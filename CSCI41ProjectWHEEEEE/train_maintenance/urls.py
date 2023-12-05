from django.urls import path
from .views import MaintenanceListView, TrainMaintenanceTasksView, TaskMasterListView

urlpatterns = [
    path('', MaintenanceListView, name='homeView'),
    path('<int:pk>/maintenanceTasks', TrainMaintenanceTasksView, name='TaskView'),
    path('', TaskMasterListView, name='TaskMasterListView'),
]

# This might be needed, depending on your Django version
app_name = "train_maintenance"