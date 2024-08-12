from django.db import models

from .questions import OutcomeQuestions
from .ecology import ExternalEcology, InternalEcology

from user.helpers.status import outcome_active_tasks


class Outcome(models.Model):
    o_questions = models.OneToOneField(
        OutcomeQuestions,
        on_delete=models.CASCADE,
        default='Not answered at all',
        related_name='o_questions',
        null=False,
        blank=False
    )
    ie_questions = models.OneToOneField(
        InternalEcology,
        on_delete=models.CASCADE,
        default='Not answered at all',
        related_name='ie_questions',
        null=False,
        blank=False
    )
    ee_questions = models.OneToOneField(
        ExternalEcology,
        on_delete=models.CASCADE,
        default='Not answered at all',
        related_name='ee_questions',
        null=False,
        blank=False
    )

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_task_done_at = models.DateTimeField(null=True, blank=True)
    is_achieved = models.BooleanField(default=False)
    achieved_at = models.DateTimeField(default=None, null=True)
    is_hided = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} | XP:'

    def active_tasks(self):
        return outcome_active_tasks(self.pk)

    def total_xp(self):
        level = 0
        for i in self.classic_tasks.filter(is_done=True):
            level += i.xp

        for i in self.deadline_tasks.all():
            if i.is_aborted is True:
                level -= i.penalty_xp
            if i.is_done is True:
                level += i.xp

        for i in self.count_tasks.all():
            xp = i.total_count * i.xp
            level += xp

        for i in self.time_tasks.all():
            xp = i.total_time / 60 * i.xp
            level += round(xp)

        return level

