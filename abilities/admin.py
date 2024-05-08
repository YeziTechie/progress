from django.contrib import admin

from .models.ability import Ability


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'total_xp',
        'created_at',
        'last_task_done_at',
    )
    search_fields = (
        'name',
    )

