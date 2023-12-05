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

        train_ids = mtrain.values_list('train_id', flat=True)
        trainHere = TRAIN.objects.filter(Train_ID__in=train_ids)
        modelss = trainHere.values_list('Model', flat=True)
        trainMhere = TRAIN_MODEL.objects.filter(Model__in=modelss)

        task_ids = mtask.values_list('task_id', flat=True)
        taskHere = TASK.objects.filter(Task_id__in=task_ids)
        
        print(taskHere)
        print(MAINTENANCE_LOGS.objects.all())

        return render(request, 'train_maintenance/Task-Train_Model.html', {"tasks":taskHere, "train":trainMhere[0]})

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

