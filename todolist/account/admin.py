from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "is_active", "is_staff", "is_verified"]
    list_filter = ["email", "is_active", "is_staff", "is_verified"]

    # for fields show ditale user
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "is_superuser", "is_verified")},
        ),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    # fields for add new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_verified",
                ),
            },
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
