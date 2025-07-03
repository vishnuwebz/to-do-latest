from django.contrib import admin
from .models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'priority', 'due_date', 'created')
    list_filter = ('completed', 'priority', 'due_date')
    search_fields = ('title',)
    date_hierarchy = 'created'