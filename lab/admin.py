from django.contrib import admin

# Register your models here.
from .models import Lab, LabProfile, LabProfile, LabService, ImageAlbum

admin.site.register(Lab)
admin.site.register(LabProfile)
admin.site.register(LabService)
admin.site.register(ImageAlbum)