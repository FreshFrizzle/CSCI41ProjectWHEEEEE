from django.contrib import admin
from .models import CUSTOMER, TICKET, TRIP, TRIP_LOGS, STATION

class CustomerAdmin(admin.ModelAdmin):
    model = CUSTOMER

class TicketAdmin(admin.ModelAdmin):
    model = TICKET

class TripAdmin(admin.ModelAdmin):
    model = TRIP

class Trip_LogsAdmin(admin.ModelAdmin):
    model = TRIP_LOGS

class StationAdmin(admin.ModelAdmin):
    model = STATION

admin.site.register(CUSTOMER, CustomerAdmin)
admin.site.register(TICKET, TicketAdmin)
admin.site.register(TRIP, TripAdmin)
admin.site.register(TRIP_LOGS, Trip_LogsAdmin)
admin.site.register(STATION, StationAdmin)
