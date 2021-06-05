from django.shortcuts import render, redirect
from .models import Lab, LabService
from django.contrib import messages
from django.views.generic import ListView


# Create your views here.


def RegisterLab(request):
    if request.method == "POST":
        labname = request.POST["labname"]
        licence_no = request.POST["licence_no"]
        exp_date = request.POST["exp_date"]
        provience_no = request.POST["provience_no"]
        district = request.POST["district"]
        rural_municipality = request.POST["rural_municipality"]
        ward_no = request.POST["ward_no"]
        tole_area_apmnt = request.POST["tole_area_apmnt"]
        telephone_no = request.POST["telephone_no"]
        pan_vat_no = request.POST["labname"]
        org_type = request.POST["org_type"]
        your_role = request.POST["your_role"]

        lab = Lab.objects.create(
            labname=labname,
            licence_no=licence_no,
            exp_date=exp_date,
            provience_no=provience_no,
            district=district,
            rural_municipality=rural_municipality,
            ward_no=ward_no,
            tole_area_apmnt=tole_area_apmnt,
            telephone_no=telephone_no,
            org_type=org_type,
            pan_vat_no=pan_vat_no,
            your_role=your_role,
        )

        lab.save()
        messages.success(request, "Registered! wait for Approval")
        return redirect("labdashboard")

    else:

        return render(request, "lab/register-lab.html")


def labDashboard(request):
    form = Lab.objects.values("labname")
    context = {"form": form}
    return render(request, "lab/dashboard.html", context)


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


class LabServices(ListView):
    model = LabService
    template_name = "lab/services.html"
    context_object_name = "services"
    ordering = ["-date_created"]


def Services(request):
    return render(request, "lab/services.html")


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
