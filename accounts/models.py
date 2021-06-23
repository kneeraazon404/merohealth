import os

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

#! Account manager
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


#! Custom  Users Model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=255, blank=True, verbose_name="first_name")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="last name")
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


#! Users Profile Model


class Profile(models.Model):

    #! Model Fields Below
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        max_length=255,
        upload_to="Profile_Images",
        null=True,
        blank=True,
        default="Profile_Images/default.jpg",
    )
    birthday = models.DateTimeField(verbose_name="birthday", null=True, blank=True)
    height = models.IntegerField(verbose_name="height", null=True, blank=True)
    weight = models.IntegerField(verbose_name="weight", null=True, blank=True)
    blood_type = models.CharField(
        verbose_name="blood",
        blank=True,
        null=True,
        max_length=255,
        default="A+",
    )
    gender = models.CharField(
        verbose_name="gender",
        blank=True,
        null=True,
        max_length=255,
        default="Male",
    )
    origin = models.CharField(
        verbose_name="Origin",
        blank=True,
        null=True,
        max_length=255,
        default="Nepali",
    )
    ward_no = models.IntegerField(
        null=True,
        blank=True,
    )
    local_area = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    municipality = models.CharField(
        verbose_name="municip",
        max_length=100,
        default="Lamachaur",
    )
    provience = models.CharField(
        max_length=200,
        verbose_name="provience",
        default="3",
    )
    district = models.CharField(
        max_length=200,
        verbose_name="Disctrict",
        default="Kaski",
    )
    smoking = models.CharField(
        verbose_name="smoking",
        max_length=100,
        default="No",
    )
    alchol = models.CharField(
        verbose_name="alchol",
        max_length=100,
        default="No",
    )
    drug = models.CharField(
        verbose_name="Drug",
        max_length=100,
        default="No",
    )
    social_links_fb = models.CharField(
        verbose_name="Facebook", max_length=100, null=True, blank=True
    )

    social_links_tw = models.CharField(
        verbose_name="Twitter", max_length=100, null=True, blank=True
    )
    social_links_ins = models.CharField(
        verbose_name="Instagram", max_length=100, null=True, blank=True
    )
    social_links_yt = models.CharField(
        verbose_name="Personal Site", max_length=100, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
