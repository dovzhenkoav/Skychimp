from django.contrib import admin

from app_users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'surname', 'is_active')
    list_filter = ('email', 'first_name', 'last_name', 'surname', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
