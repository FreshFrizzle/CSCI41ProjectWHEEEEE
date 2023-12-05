from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from CSCI41ProjectWHEEEEE.train_operator.models import TRAIN_MODEL
# Create your views here.


def MaintenanceListView(request):
    return render(request, 'train_maintenance/Train_model-Maintenace.html', {"trains":TRAIN_MODEL.objects.all()})

class TrainMaintenanceTasksView(View):
    #list down the task for the given train model
    def get(self, request, maintenance_ID=None, *args, **kwargs):

        #train_model and train_ID are one-to-one
        train_model = self.request.GET.get('Model')

        #get tasks related to the train_model
        maintenance_tasks = train_model.maintenance_num_set.all()
        tasks = maintenance_tasks.task_id.all()

        return render(request, 'train_maintenance/Task-Train_Model.html', {"train_model":train_model, "tasks":tasks})

