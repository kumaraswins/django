from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = 'Project'
admin.site.site_title = 'Project'