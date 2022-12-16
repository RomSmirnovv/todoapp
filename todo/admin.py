from django.contrib import admin
from .models import Todo, Status


class TodoAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'content', 'time_create', 'time_update', 'is_published', 'status')
	list_display_links = ('id', 'title')
	search_field = ('id', 'title', 'description', 'content', 'status')
	list_editable = ('status',)
	list_filter = ('status',)

admin.site.register(Todo, TodoAdmin)

class StatusAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	search_field = ('id', 'name')

admin.site.register(Status, StatusAdmin)