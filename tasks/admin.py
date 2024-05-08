from django.contrib import admin
from .models.task import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'ability',
        'xp',
        'is_done',
        'done_at',
        'created_at',
        'is_added'
    ]
    search_fields = (
        'ability',
        'is_done',
        'is_added'
    )
