from django.shortcuts import render, redirect
from .models import Lab, LabService, ImageAlbum
from django.contrib import messages
from django.views.generic import ListView
from .forms import LabMember
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .emails import Emails, EmailToAdmin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

#! Lab Register View
@login_required
def RegisterLab(request):
    user = request.user
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
        Emails(request)
        EmailToAdmin(request)
        messages.success(request, "Registered! wait for Approval")
        return redirect("labdashboard")

    else:

        return render(request, "lab/register-lab.html")


#! Lab Dashboard View
@login_required
def labDashboardView(request):
    user = request.user
    form = Lab.objects.all()
    is_verified = user.lab.is_verified
    if is_verified == True:
        context = {"form": form}
        return render(request, "lab/dashboard.html", context)
    else:
        messages.error(request, "Your lab Has Not been Verified Yet")
        return redirect("home")


#! Lab Profile view
@login_required
def LabProfileView(request):
    user = request.user
    form = Lab.objects.all()
    # is_active = Lab.objects.values("is_active")
    # if is_active == True:
    context = {"form": form}
    return render(request, "lab/lab-profile.html", context)
    # else:
    #     messages.error(request, "Your lab Has Not been Verified Yet")
    #     return redirect("home")


#! Lab Profile public view
def LabProfilePublicView(request):
    form = Lab.objects.all()
    # is_active = Lab.objects.values("is_active")
    # if is_active == True:
    context = {"form": form}
    return render(request, "lab/lab-profile-public-view.html", context)
    # else:
    #     messages.error(request, "Your lab Has Not been Verified Yet")
    #     return redirect("home")


# ! Lab Member Management Views
class memberListView(ListView):
    model = LabMember
    template_name = "lab/lab-member.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "members"
    ordering = ["-date_added"]
    paginate_by = 5


class userSmemberListView(ListView):
    model = LabMember
    template_name = "lab/lab-member.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "members"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return LabMember.objects.filter(author=user).order_by("-date_posted")


class memberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LabMember
    fields = ["__all__"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class memberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LabMember
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def members(request):
    return render(
        request,
        "lab/lab-member.html",
    )


#! Lab Services Views
class servicesListView(ListView):
    model = LabService
    template_name = "lab/services.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "services"
    ordering = ["-date_created"]
    paginate_by = 5


class userServicesListView(ListView):
    model = LabService
    template_name = "lab/services.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "services"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return LabMember.objects.filter(author=user).order_by("-date_posted")


class servicesDetailView(DetailView):
    model = LabService


class serviceCreateView(LoginRequiredMixin, CreateView):
    model = LabService
    fields = ["__all__"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class serviceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LabMember
    fields = ["__all__"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class serviecDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LabMember
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def services(request):
    return render(request, "lab/serivices.html", {"title": "About"})


def healthPackage(request):
    return render(request, "lab/health-package.html")


def Payments(request):
    return render(request, "lab/payments.html")


def Reports(request):
    return render(request, "lab/reports.html")


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
