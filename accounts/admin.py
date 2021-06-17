from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

from .models import Profile

# Register your models here.
admin.site.register(Profile)


class AccountAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
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
        "first_name",
    )
    readonly_fields = (
        "id",
        "date_joined",
        "last_login",
    )
    list_display_links = ("first_name", "email", "username")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
