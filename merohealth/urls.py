from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("accounts/", include("accounts.urls")),
    path("lab/", include("lab.urls")),
    path("verification/", include("verify_email.urls")),
]
