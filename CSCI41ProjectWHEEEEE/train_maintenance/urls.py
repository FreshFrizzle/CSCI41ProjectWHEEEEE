from django.urls import path
from .views import MaintenanceListView, TrainTasksView, TaskMasterListView, TrainMasterListView, TrainMaintenanceView

urlpatterns = [
    path('maintenance/', MaintenanceListView, name='homeView'),
    path('trains/<int:pk>/tasks', TrainTasksView.as_view(), name='TrainTaskView'),
    path('tasks/', TaskMasterListView, name='TaskMasterListView'),
    path('trains/', TrainMasterListView, name='TrainMasterListView'),
    path('trains/<int:pk>/maintenance', TrainMaintenanceView.as_view(), name='TrainMaintenanceView'),
]

# This might be needed, depending on your Django version
app_name = "train_maintenance"