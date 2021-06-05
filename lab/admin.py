from django.contrib import admin

# Register your models here.
from .models import Lab, LabProfile, LabProfile, LabService

admin.site.register(Lab)
admin.site.register(LabProfile)
admin.site.register(LabService)