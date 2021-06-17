from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    #     EmailVerificationView,
    #     UserProfileView,
    #     BlogView,
    #     ConfirmRequestView,
    #     DoctorAppointments,
    #     DoctorPrescriptions,
    #     LabAppointments,
    #     productOrders,
    #     labReports,
    #     labRequests,
    #     mySettings,
    #     testRequests,
)


urlpatterns = [
    path("login/", LoginView, name="login"),
    path("register/", RegisterView, name="register"),
    # path("logout/", views.logout, name="logout"),
    # path("profile/", views.profile, name="profile"),
    # path("register/", RegistrationView, name="register"),
    # path("login/", LoginView, name="login"),
    # path("verification/", EmailVerificationView, name="verification"),
    # path("profile/", UserProfileView, name="profile"),
    # path("blog/", BlogView, name="blog"),
    # path("confirm-request/", ConfirmRequestView, name="confirm-request"),
    # path("doctor-appointments/", DoctorAppointments, name="doctor-appointments"),
    # path("prescriptions/", DoctorPrescriptions, name="prescriptions"),
    # path("lab-appointments/", LabAppointments, name="lab-appointments"),
    # path("lab-requests/", labRequests, name="lab-requests"),
    # path("lab-reports/", labReports, name="lab-reports"),
    # path("product-orders/", productOrders, name="product-orders"),
    # path("my-settings/", mySettings, name="my_settings"),
    # path("test-requests/", testRequests, name="test-requests"),
]
