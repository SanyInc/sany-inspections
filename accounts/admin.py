from django.contrib import admin
from .models import User, Customer, HealthRegulator, BusinessOwner, Inspector, Admin, Moderator
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'role', 'created_by')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password',  )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'role', 'created_by'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login', )


class HealthRegulatorAdmin(admin.ModelAdmin):
    list_display = ("user", "store", "created_by", )



admin.site.register(User, UserAdmin)

admin.site.register(Customer)
admin.site.register(BusinessOwner)
admin.site.register(Admin)
admin.site.register(Moderator)
admin.site.register(Inspector)
admin.site.register(HealthRegulator, HealthRegulatorAdmin)