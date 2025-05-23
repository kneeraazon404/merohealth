import json

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from validate_email import validate_email
from verify_email.email_handler import send_verification_email

from .forms import AccountAuthenticationForm, UserRegisterForm, UserProfileUpdateForm


#! Email Validation view
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]
        if not validate_email(email):
            return render({"email_error": "Email is invalid"}, status=400)
        if User.objects.filter(email=email).exists():
            return render(
                {"email_error": "sorry email in use,choose another one "}, status=409
            )
        return render({"email_valid": True})


#! Username validation View
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]
        if not str(username).isalnum():
            return render(
                {
                    "username_error": "username should only contain alphanumeric characters"
                },
                status=400,
            )
        if User.objects.filter(username=username).exists():
            return render(
                {"username_error": "sorry username in use,choose another one "},
                status=409,
            )
        return render({"username_valid": True})


UserModel = get_user_model()

#! User Register View
@csrf_exempt
def RegisterView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return render("You are already authenticated as " + str(user.username))

    context = {}
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            inactive_user = send_verification_email(request, form)
            messages.success(request, "Successfully registered | Activate Your Account")
            return redirect("login")
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


#! User's Profile view
@login_required
def UserProfileView(request):
    return render(request, "accounts/user-profile.html")


#! User's Profile update view
def UpdateProfileView(request):
    if request.method == "POST":
        form = UserProfileUpdateForm()
        # context = {"form": form}
    return render(request, "accounts/update_profile.html")


def BlogView(request):
    return render(request, "accounts/blog.html")


def UserDashboardView(request):
    return render(request, "accounts/dashboard.html")


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


def TestRequests(request):
    return render(request, "accounts/test-requests.html")
