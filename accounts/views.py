import datetime

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Account
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            if Account.objects.filter(username=username).exists():
                messages.error(request, "Username already in use")
                return redirect("register")
            elif Account.objects.filter(email=email).exists():
                messages.error(request, "email already use")
                return redirect("register")

            elif password1 != password2:
                messages.error(request, "Passwords didn't match")
                return redirect("register")

            if len(password1) < 8:
                messages.error(request, "Password too shrt")
                return redirect("register")

        messages.success(
            request,
            f"Your account has been created for {username}! Activate your account",
        )
        return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password1"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("home")
    return render(request, "accounts/logout.html")


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "accounts/profile.html", context)


def LoginView(request):
    return render(request, "accounts/login.html")


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
