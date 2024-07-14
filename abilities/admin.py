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

    def set_xp_to_zero(modeladmin, request, queryset):
        queryset.update(total_xp=0)
        modeladmin.message_user(request, "Selected outcome's xp has set to zero")

    set_xp_to_zero.short_description = "Set xp to Zero"

    actions = [
        set_xp_to_zero,
    ]
