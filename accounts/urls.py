from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    #     EmailVerificationView,
    UserProfileView,
    #     BlogView,
    #     ConfirmRequestView,
    #     DoctorAppointments,
    #     DoctorPrescriptions,
    #     LabAppointments,
    #     productOrders,
    #     labReports,
    #     labRequests,
    UpdateProfileView,
    #     testRequests,
)


urlpatterns = [
    path("login/", LoginView, name="login"),
    path("register/", RegisterView, name="register"),
    path("logout/", LogoutView, name="logout"),
    #! profile
    path("profile/", UserProfileView, name="profile"),
    path("update_profile/", UpdateProfileView, name="update_profile"),
    # ? Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # path("blog/", BlogView, name="blog"),
    # path("confirm-request/", ConfirmRequestView, name="confirm-request"),
    # path("doctor-appointments/", DoctorAppointments, name="doctor-appointments"),
    # path("prescriptions/", DoctorPrescriptions, name="prescriptions"),
    # path("lab-appointments/", LabAppointments, name="lab-appointments"),
    # path("lab-requests/", labRequests, name="lab-requests"),
    # path("lab-reports/", labReports, name="lab-reports"),
    # path("product-orders/", productOrders, name="product-orders"),
    # path("test-requests/", testRequests, name="test-requests"),
]
