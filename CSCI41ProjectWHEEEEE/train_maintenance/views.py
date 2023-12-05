from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from CSCI41ProjectWHEEEEE.train_operator.models import TRAIN_MODEL
from CSCI41ProjectWHEEEEE.train_maintenance.models import TASK, MAINTENANCE
# Create your views here.


def MaintenanceListView(request):
    return render(request, 'train_maintenance/Train_model-Maintenace.html', {"Maintenance":MAINTENANCE.objects.all()})

class TrainTasksView(View):
    #list down the task for the given train model
    def get(self, request, maintenance_ID=None, *args, **kwargs):

        #train_model and train_ID are one-to-one
        train_model = self.request.GET.get('Model')

        #get tasks related to the train_model
        maintenance_tasks = train_model.maintenance_num_set.all()
        tasks = maintenance_tasks.task_id.all()

        return render(request, 'train_maintenance/Task-Train_Model.html', {"train_model":train_model, "tasks":tasks})

def TaskMasterListView(request):
    return render(request, 'train_maintenance/Task_masterlist.html', {"tasks":TASK.objects.all()})

def TrainMasterListView(request):
    return render(request, 'train_maintenance/Task_masterlist.html', {"train":TRAIN_MODEL.objects.all()})

class TrainMaintenanceView(View):
    def get(self, request, maintenance_ID=None, *args, **kwargs):

        #train_model and train_ID are one-to-one
        train_model = self.request.GET.get('Model')

        #get tasks related to the train_model
        maintenance_task = train_model.maintenance_num_set.all()
        maintenance = maintenance_task.maintenance_num.all()

        return render(request, 'train_maintenance/Task-Train_Model.html', {"train_model":train_model, "Maintenance":maintenance})

