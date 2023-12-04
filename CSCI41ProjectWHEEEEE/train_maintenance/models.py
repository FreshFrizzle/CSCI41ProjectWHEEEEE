from django.db import models

# Create your models here.
class TRAIN(models.Model):
    Train_ID = models.CharField(primary_key=True, max_length=6, default="000001")
    Model = models.OneToOneField(
        
    )

class TRAIN_MODEL(models.Model):
    pass

class ROUTE(models.Model):
    pass

class S_SERIES(models.Model):
    pass

class A_SERIES(models.Model):
    pass

class LOCAL(models.Model):
    pass

class INTER_TOWN(models.Model):
    pass

class S_SERIES_ROUTING(models.Model):
    pass

class A_SERIES_ROUTING(models.Model):
    pass