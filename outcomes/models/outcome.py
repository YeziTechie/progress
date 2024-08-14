from django.db import models

from .ecology import ExternalEcology, InternalEcology
from .questions import OutcomeQuestions

from user.helpers.generate_level import calculate_level

class Outcome(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_task_done_at = models.DateTimeField(null=True, blank=True)
    is_achieved = models.BooleanField(default=False)
    achieved_at = models.DateTimeField(default=None, null=True, blank=True)
    is_hided = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not hasattr(self, 'internal_ecology'):
            InternalEcology.objects.create(outcome=self)
        if not hasattr(self, 'outcome_questions'):
            OutcomeQuestions.objects.create(outcome=self)
        if not hasattr(self, 'external_ecology'):
            ExternalEcology.objects.create(outcome=self)

    def __str__(self):
        return f'{self.name} | XP:'

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

    def level(self):
        return calculate_level(self.total_xp())

    def active_tasks(self):

        classics = self.classic_tasks.filter(outcome=self)
        deadlines = self.deadline_tasks.filter(outcome=self)
        counts = self.count_tasks.filter(outcome=self)
        times = self.time_tasks.filter(outcome=self)

        result = 0
        result += len(times) + len(counts)

        for classic in classics:
            if classic.is_done is False:
                result += 1

        for deadline in deadlines:
            if deadline.is_done is False:
                result += 1

        return result


