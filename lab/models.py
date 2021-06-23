from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE, SET_NULL


class Lab(models.Model):
    founder = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
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
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.labname


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()


class LabProfile(models.Model):
    lab = models.OneToOneField(Lab, on_delete=SET_NULL, null=True)
    cover_img = models.ImageField(
        verbose_name="cover image",
        upload_to="lab-images/cover-images",
        default="profile.jpg",
    )
    gallery = models.ForeignKey(
        ImageAlbum,
        related_name="images",
        on_delete=models.CASCADE,
    )
    youtube = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return "Lab profile"


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

    def __str__(self):
        return self.platelet_count


class LabMember(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full name")
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, blank=True)
    profile_image = models.ForeignKey(
        ImageAlbum,
        related_name="profile_pics",
        on_delete=models.CASCADE,
    )
    position = models.CharField(max_length=500)
    qualification = models.CharField(max_length=500)
    bio = models.TextField(verbose_name="Biograph")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class healthPackage(models.Model):
    package_name = models.CharField(max_length=100, verbose_name="Full name")
    total_price = models.FloatField(max_length=100, verbose_name="total price")
    discount_price = models.FloatField(max_length=100, verbose_name="discount price")
    package_includes = models.CharField(max_length=500, verbose_name="package includes")
    package_description = models.TextField(
        max_length=500, verbose_name="package description"
    )

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name
