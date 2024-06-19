from django.contrib import admin
from .models.task import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'xp',
        'is_done',
        'done_at',
        'created_at',
        'is_added'
    ]
    search_fields = (
        'outcome',
        'is_done',
        'is_added'
    )
