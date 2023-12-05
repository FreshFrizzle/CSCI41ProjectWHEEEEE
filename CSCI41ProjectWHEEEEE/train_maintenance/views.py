from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from train_operator.models import TRAIN, TRAIN_MODEL
from train_maintenance.models import TASK, MAINTENANCE, MAINTENANCE_LOGS, MAINTENANCE_TASK
# Create your views here.


def MaintenanceListView(request):
    return render(request, 'train_maintenance/Maintenance_Logs.html', {"Maintenance":MAINTENANCE.objects.all()})

class TrainTasksView(View):
    #list down the task for the given train model
    def get(self, request, pk):

        #get tasks related to the train_model
        print(pk)
        mtrain = MAINTENANCE_LOGS.objects.filter(maintenance_num=pk)
        mtask = MAINTENANCE_TASK.objects.filter(maintenance_num=pk)
        print(list(mtrain))

        #trainAll = TRAIN.objects.all()

        trainHere = mtrain.select_related('train_id')[0]
        taskHere = mtask.select_related('task_id')[0]
        print(trainHere)
        #tasks = mtask.objects.get(task_id=pk)

        return render(request, 'train_maintenance/Task-Train_Model.html', {"tasks":taskHere, "train":trainHere})

def TaskMasterListView(request):
    return render(request, 'train_maintenance/Task_masterlist.html', {"tasks":TASK.objects.all()})

def TrainMasterListView(request):
    return render(request, 'train_maintenance/Train_masterlist.html', {"trains":TRAIN.objects.all(), "train_model":TRAIN_MODEL.objects.all() })

class TrainMaintenanceView(View):
    def get(self, request, pk):

        #get tasks related to the train_model
        print(pk)
        mtrain = MAINTENANCE_LOGS.objects.filter(maintenance_num=pk)
        print(list(mtrain))

        #get tasks related to the train_model
        maintenace_train = mtrain.select_related('train_id')[0]

        return render(request, 'train_maintenance/Task-Train_Model.html', {"train_model":maintenace_train, "Maintenance":maintenace_train})

