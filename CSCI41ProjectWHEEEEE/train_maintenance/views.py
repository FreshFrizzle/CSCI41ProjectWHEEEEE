from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from train_operator.models import TRAIN, TRAIN_MODEL
from train_maintenance.models import TASK, MAINTENANCE, MAINTENANCE_LOGS, MAINTENANCE_TASK
# Create your views here.


def MaintenanceListView(request):
    postMaintenance = MAINTENANCE.objects.raw("SELECT * FROM train_maintenance_maintenance")

    return render(request, 'train_maintenance/Maintenance_Logs.html', {"Maintenance":postMaintenance})

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
        print(trainMhere)

        return render(request, 'train_maintenance/Task-Train_Model.html', {"tasks":taskHere, "train":trainMhere[0]})

def TaskMasterListView(request):
    postTask = TASK.objects.raw("SELECT * FROM train_maintenance_task")

    return render(request, 'train_maintenance/Task_masterlist.html', {"tasks":postTask})

def TrainMasterListView(request):
    postTrainM = TRAIN_MODEL.objects.raw("SELECT * FROM train_operator_train_model")

    return render(request, 'train_maintenance/Train_masterlist.html', {"trains":TRAIN.objects.all(), "train_model":postTrainM})

class TrainMaintenanceView(View):
    def get(self, request, pk):

        print(pk)
     
        trainHere = TRAIN.objects.filter(Model__exact=pk)
        modelss = trainHere.values_list('Model', flat=True)
        trainMhere = TRAIN_MODEL.objects.filter(Model__in=modelss)
        print(trainHere)
        mlogs = MAINTENANCE_LOGS.objects.filter(train_id__in=trainHere.values_list('Train_ID', flat=True))
        print(mlogs)
        maintenances = MAINTENANCE.objects.filter(maintenance_num__in=mlogs.values_list('maintenance_num', flat=True))
        print(maintenances)
        

        return render(request, 'train_maintenance/Maintenance-Train_Model.html', {"trainModel":trainMhere[0], "Maintenance":maintenances})

