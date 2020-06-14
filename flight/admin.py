from django.contrib import admin

# Register your models here.
from .models import Airport,Flight,Passengers
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passengers)
