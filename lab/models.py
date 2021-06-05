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
    cover_img = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        default="profile.jpg",
    )
    logo_img = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )
    gallery_image0 = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )

    gallery_img1 = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )
    gallery_img2 = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )
    gallery_img3 = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )
    gallery_img4 = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        blank=True,
        null=True,
        default="profile.jpg",
    )
    youtube = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)


class LabService(models.Model):
    platelet_count = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="palate count",
    )
    category_name = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name="catefory name",
    )
    test_cost = models.FloatField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="test cost",
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
