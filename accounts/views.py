import datetime
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from verify_email.email_handler import send_verification_email

# from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Account
from .forms import UserRegisterForm, AccountAuthenticationForm, UserUpdateForm

UserModel = get_user_model()
#! Register View
def RegisterView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return render("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            is_active = form.cleaned_data.get("is_active")
            email = form.cleaned_data.get("email").lower()
            raw_password = form.cleaned_data.get("password1")
            is_active = send_verification_email(request, form)
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            destination = kwargs.get("next")
            if destination:
                messages.success(
                    request, "Successfully registered | Activate Your Account"
                )
                return redirect(destination)
            return redirect("login")
        else:
            context = {"form": form}

    else:
        form = UserRegisterForm()
        context = {"form": form}
    return render(request, "accounts/register.html", context)


#! Login View
def LoginView(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                messages.success(request, "Logged in Successfully")
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context["form"] = form

    return render(request, "accounts/login.html", context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


#! Logout View
def LogoutView(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect("home")


# @login_required
# def profile(request):
#     if request.method == "POST":
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=request.user.profile
#         )
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"Your account has been updated!")
#             return redirect("profile")

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {"u_form": u_form, "p_form": p_form}

#     return render(request, "accounts/profile.html", context)


def EmailVerificationView(request):
    return render(request, "accounts/verify-email.html")


def UserProfileView(request):
    return render(request, "accounts/user-profile.html")


def BlogView(request):
    return render(request, "accounts/blog.html")


def ConfirmRequestView(request):
    return render(request, "accounts/confirm-request.html")


def DoctorAppointments(request):
    return render(request, "accounts/doctor-appointment.html")


def DoctorPrescriptions(request):
    return render(request, "accounts/doctor-prescriptions.html")


def LabAppointments(request):
    return render(request, "accounts/lab-appointments.html")


def labReports(request):
    return render(request, "accounts/lab-reports.html")


def labRequests(request):
    return render(request, "accounts/lab-requests.html")


def productOrders(request):
    return render(request, "accounts/product-orders.html")


def testRequests(request):
    return render(request, "accounts/test-requests.html")


def mySettings(request):
    return render(request, "accounts/my-settings.html")
