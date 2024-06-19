from django.contrib import admin

from .models.outcome import Outcome


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'total_xp',
        'created_at',
        'last_task_done_at',
    )
    search_fields = (
        'name',
    )

