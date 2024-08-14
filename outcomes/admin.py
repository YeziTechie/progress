from django.contrib import admin

from .models.outcome import Outcome
from .models.ecology import InternalEcology, ExternalEcology
from .models.questions import OutcomeQuestions


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'last_task_done_at',
    )
    search_fields = (
        'name',
    )


@admin.register(OutcomeQuestions)
class OutcomeQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'outcome',
        'positive'
    )
    search_fields = (
        'outcome',
        'positive'
    )


@admin.register(InternalEcology)
class InternalEcologyAdmin(admin.ModelAdmin):
    list_display = (
        'outcome',
        'q1'
    )
    search_fields = (
        'outcome',
        'q1'
    )


@admin.register(ExternalEcology)
class ExternalEcologyAdmin(admin.ModelAdmin):
    list_display = (
        'outcome',
        'q1'
    )
    search_fields = (
        'outcome',
        'q1'
    )