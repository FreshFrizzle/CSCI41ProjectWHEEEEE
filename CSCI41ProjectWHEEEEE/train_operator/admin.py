from django.contrib import admin

from .models import TRAIN_MODEL, TRAIN, ROUTE, S_SERIES,S_SERIES_ROUTING, A_SERIES, A_SERIES_ROUTING,LOCAL,INTER_TOWN

class Train_ModelAdmin(admin.ModelAdmin):
    model = TRAIN_MODEL

class TrainAdmin(admin.ModelAdmin):
    model = TRAIN

class RouteAdmin(admin.ModelAdmin):
    model = ROUTE

class S_SeriesAdmin(admin.ModelAdmin):
    model = S_SERIES

class S_Series_RoutingAdmin(admin.ModelAdmin):
    model = S_SERIES_ROUTING

class A_SeriesAdmin(admin.ModelAdmin):
    model = A_SERIES

class A_Series_RoutingAdmin(admin.ModelAdmin):
    model = A_SERIES_ROUTING

class LocalAdmin(admin.ModelAdmin):
    model = LOCAL

class Inter_TownAdmin(admin.ModelAdmin):
    model = INTER_TOWN

admin.site.register(TRAIN_MODEL, Train_ModelAdmin)
admin.site.register(TRAIN, TrainAdmin)
admin.site.register(ROUTE, RouteAdmin)
admin.site.register(S_SERIES, S_SeriesAdmin)
admin.site.register(S_SERIES_ROUTING, S_Series_RoutingAdmin)
admin.site.register(A_SERIES, A_SeriesAdmin)
admin.site.register(A_SERIES_ROUTING, A_Series_RoutingAdmin)
admin.site.register(LOCAL, LocalAdmin)
admin.site.register(INTER_TOWN, Inter_TownAdmin)