from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "full_name",
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
    )
    search_fields = (
        "email",
        "username",
        "full_name",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )
    list_display_links = ("full_name", "email", "username")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
