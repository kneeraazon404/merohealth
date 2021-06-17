from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if password1 == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used")
                    return redirect("register")
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username,
                        password=password1,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        # phone=phone,
                    )
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, "You are now registered! Activate Account"
                    )
                    return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")


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
