from django.shortcuts import render

# Create your views here.
def labDashboard(request):
    return render(request, "lab/dashboard.html")


def healthPackage(request):
    return render(request, "lab/health-package.html")


def labMember(request):
    return render(request, "lab/lab-member.html")


def labProfile(request):
    return render(request, "lab/lab-profile.html")


def Payments(request):
    return render(request, "lab/payments.html")


def Reports(request):
    return render(request, "lab/reports.html")


def Services(request):
    return render(request, "lab/services.html")


def RegisterLab(request):
    return render(request, "lab/register-lab.html")


def TestRequests(request):
    return render(request, "lab/test-requests.html")


def TestRequestsCollectorView(request):
    return render(request, "lab/test-requests-collector-view.html")


def TestRequestsCompleted(request):
    return render(request, "lab/test-requests-completed.html")


def TestRequestsRunningProcess(request):
    return render(request, "lab/test-requests-running-process.html")


def TestRequestsRunning(request):
    return render(request, "lab/test-requests-running.html")
