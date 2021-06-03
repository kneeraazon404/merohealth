from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
class Lab(models.Model):
    founder = models.ManyToManyField(settings.AUTH_USER_MODEL)
    labname = models.CharField(max_length=100, blank=True)
    licence_no = models.CharField(max_length=100, blank=True)
    exp_date = models.CharField(max_length=100, blank=True)
    provience_no = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    rural_municipality = models.CharField(max_length=100, blank=True)
    ward_no = models.CharField(max_length=100, blank=True)
    tole_area_apmnt = models.CharField(max_length=100, blank=True)
    telephone_no = models.CharField(max_length=100, blank=True)
    org_type = models.CharField(max_length=100, blank=True)
    pan_vat_no = models.CharField(max_length=100, blank=True)
    your_role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.labname


class LabProfile(models.Model):
    lab = models.OneToOneField(Lab, on_delete=CASCADE)
