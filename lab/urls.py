from django.urls import path
from .views import (
    RegisterLab,
    Reports,
    Services,
    TestRequests,
    labDashboard,
    healthPackage,
    labMember,
    labProfile,
    Payments,
    TestRequestsRunningProcess,
    TestRequestsCompleted,
    TestRequestsCollectorView,
    TestRequestsRunning,
)

urlpatterns = [
    path("dashboard/", labDashboard, name="labdashboard"),
    path("health-package/", healthPackage, name="health-package"),
    path("lab-member/", labMember, name="lab-member"),
    path("lab-profile/", labProfile, name="lab-profile"),
    path("payments/", Payments, name="payments"),
    path("services/", Reports, name="services"),
    path("reports/", Services, name="reports"),
    path("register/", RegisterLab, name="registerlab"),
    path("test-requests/", TestRequests, name="test-request"),
    path("collector/", TestRequestsCollectorView, name="collector"),
    path("completed/", TestRequestsCompleted, name="completed"),
    path("running-process/", TestRequestsRunningProcess, name="running-process"),
    path("running/", TestRequestsRunning, name="running"),
]
