from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerUserCreationForm, CustomerUserChangeForm

# Register your models here.
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_superuser"]


admin.site.register(CustomUser, CustomUserAdmin)
