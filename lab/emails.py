# ? Default message/alert function
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.conf import settings

#! Lab Activation email to the admin
def EmailToAdmin(request):
    user = request.user
    sender = settings.EMAIL_HOST_USER
    send_mail(
        "New Lab Registered! Activation  Needed!!",
        "Please go through the link http://localhost:8000/admin/lab/lab/ to activate the lab  freshly registered",
        sender,
        ["karkinirajan1999@gmail.com"],
        fail_silently=False,
    )
    return


# ? Default message/alert function
def Emails(request):
    user = request.user
    sender = settings.EMAIL_HOST_USER
    send_mail(
        "Lab Register Activate Needed",
        "Your lab is being Verified , We will notify you ASAP",
        sender,
        [user.email],
        fail_silently=False,
    )
    return
