# Generated by Django 3.2.4 on 2021-07-03 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='Profile_Images/default.jpg', max_length=255, null=True, upload_to='Profile_Images')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='birthday')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='height')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='weight')),
                ('blood_type', models.CharField(blank=True, default='A+', max_length=255, null=True, verbose_name='blood')),
                ('gender', models.CharField(blank=True, default='Male', max_length=255, null=True, verbose_name='gender')),
                ('origin', models.CharField(blank=True, default='Nepali', max_length=255, null=True, verbose_name='Origin')),
                ('ward_no', models.IntegerField(blank=True, null=True)),
                ('local_area', models.CharField(blank=True, max_length=100, null=True)),
                ('municipality', models.CharField(default='Lamachaur', max_length=100, verbose_name='municip')),
                ('provience', models.CharField(default='3', max_length=200, verbose_name='provience')),
                ('district', models.CharField(default='Kaski', max_length=200, verbose_name='Disctrict')),
                ('smoking', models.CharField(default='No', max_length=100, verbose_name='smoking')),
                ('alchol', models.CharField(default='No', max_length=100, verbose_name='alchol')),
                ('drug', models.CharField(default='No', max_length=100, verbose_name='Drug')),
                ('social_links_fb', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook')),
                ('social_links_lkn', models.CharField(blank=True, max_length=100, null=True, verbose_name='Linkedin')),
                ('social_links_tw', models.CharField(blank=True, max_length=100, null=True, verbose_name='Twitter')),
                ('social_links_ins', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('social_links_pws', models.CharField(blank=True, max_length=100, null=True, verbose_name='Personal Site')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
