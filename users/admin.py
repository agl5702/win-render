from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy 
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering=['email']
    add_form=CustomUserCreationForm
    form= CustomUserChangeForm
    model=User
    list_display=['email','first_name','last_name','is_active','is_staff']
    list_display_links=['email']
    list_filter=['email','first_name','last_name','is_active','is_staff']
    search_fields=['email','first_name','last_name']

    fieldsets = (
        (
            gettext_lazy("Login Credentials"), {
                "fields": ("email", "password",)
            }, 
        ),
        (
            gettext_lazy("Personal Information"),
            {
                "fields": ('first_name', 'last_name',)
            },
        ),
        (
            gettext_lazy("Permissions and Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            gettext_lazy("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
            },),
        )




admin.site.register(User,UserAdmin)