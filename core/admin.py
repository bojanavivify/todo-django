from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creation_date', 'status', 'closed_date', 'user')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Todo, TodoAdmin)
