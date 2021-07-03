from django.urls import path
from .views import (
    RegisterLab,
    Reports,
    TestRequests,
    labDashboard,
    healthPackage,
    Payments,
    TestRequestsRunningProcess,
    TestRequestsCompleted,
    TestRequestsCollectorView,
    TestRequestsRunning,
    servicesListView,
    # memberListView,
    LabProfile,
)


urlpatterns = [
    path("dashboard/", labDashboard, name="labdashboard"),
    path("profile/", LabProfile, name="labprofile"),
    path("health-package/", healthPackage, name="health-package"),
    path("payments/", Payments, name="payments"),
    path("services/", servicesListView.as_view(), name="services"),
    path("member/", servicesListView.as_view(), name="lab-member"),
    path("reports/", Reports, name="reports"),
    path("register/", RegisterLab, name="registerlab"),
    path("test-requests/", TestRequests, name="test-request"),
    path("collector/", TestRequestsCollectorView, name="collector"),
    path("completed/", TestRequestsCompleted, name="completed"),
    path("running-process/", TestRequestsRunningProcess, name="running-process"),
    path("running/", TestRequestsRunning, name="running"),
]
