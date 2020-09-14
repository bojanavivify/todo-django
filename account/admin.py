from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'address', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'email')
    list_per_page = 25


admin.site.register(User, UserAdmin)
