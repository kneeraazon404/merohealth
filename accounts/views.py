from django.shortcuts import render

# Create your views here.
def RegistrationView(request):
    return render(request, "accounts/register.html")


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
