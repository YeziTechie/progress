from django.contrib import admin
from .models.task import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'is_done',
        'is_added'
    ]
    search_fields = (
        'outcome',
        'description',
        'is_done',
        'is_added'
    )
