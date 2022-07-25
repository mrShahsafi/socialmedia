from django.contrib.admin import StackedInline, register, ModelAdmin

from django.contrib.auth.admin import UserAdmin

from django.utils.translation import ugettext_lazy as _


from core.models import (
    User,
    Profile,
)


class ProfileStackedInlineAdmin(StackedInline):
    model = Profile
    extra = 1


class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    # list_display = ('mobile',)
    # exclude = ('username',)
    model = User
    list_display = (
        "email",
        "first_name",
        "is_active",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = (
        "email",
    )


@register(User)
class BaseUserAdmin(CustomUserAdmin):
    inlines = [
        ProfileStackedInlineAdmin,
    ]
