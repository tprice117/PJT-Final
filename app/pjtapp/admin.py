from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(PrintFileStates)
admin.site.register(PrintFileStateHistory)
admin.site.register(PrintFileData)
admin.site.register(PrintFileStatus)   
