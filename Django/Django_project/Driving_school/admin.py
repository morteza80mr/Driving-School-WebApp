from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# Register your models here.

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name_user","family_name_user","National_ID_user","username", "password1", "password2","User_role"),
            },
        ),
    )
    ordering = ("username",)
    list_display = ("username","first_name_user","family_name_user", "User_role")

admin.site.register(models.Employee)
admin.site.register(models.Student)
admin.site.register(models.Document)
admin.site.register(models.Tuition)
admin.site.register(models.classroom)
admin.site.register(models.status)