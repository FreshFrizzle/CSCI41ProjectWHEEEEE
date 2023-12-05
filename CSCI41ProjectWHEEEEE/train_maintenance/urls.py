from django.urls import path
from .views import MaintenanceListView, TrainMaintenanceTasksView

urlpatterns = [
    path('', MaintenanceListView, name='homeView'),
    path('<int:pk>/maintenanceTasks', TrainMaintenanceTasksView, name='TaskView'),
]

# This might be needed, depending on your Django version
app_name = "train_maintenance"