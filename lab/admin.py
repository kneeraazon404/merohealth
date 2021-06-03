from django.contrib import admin

# Register your models here.
from .models import Lab, LabProfile, LabProfile

admin.site.register(Lab)
admin.site.register(LabProfile)