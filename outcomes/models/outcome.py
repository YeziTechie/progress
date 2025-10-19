from django.db import models
from _base import settings

from .ecology import ExternalEcology, InternalEcology
from .questions import OutcomeQuestions

from user.helpers.generate_level import calculate_level


class Outcome(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='outcomes', on_delete=models.CASCADE)
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
            if i.is_aborted:
                level -= i.penalty_xp
            if i.is_done:
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

    def deadline_active(self):
        tasks = self.deadline_tasks.filter(outcome=self)
        result = 0
        for task in tasks:
            if task.is_done is False:
                result += 1

        return result

    def classic_active(self):
        tasks = self.classic_tasks.filter(outcome=self)
        result = 0
        for task in tasks:
            if task.is_done is False:
                result += 1

        return result

    def count_active(self):
        tasks = self.count_tasks.filter(outcome=self)
        return len(tasks)

    def time_active(self):
        tasks = self.time_tasks.filter(outcome=self)
        return len(tasks)
