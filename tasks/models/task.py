from django.db import models
from abilities.models.outcome import Outcome
import datetime


class Task(models.Model):

    outcome = models.ForeignKey(
        Outcome,
        on_delete=models.SET_NULL,
        related_name='tasks_outcome',
        null=True,
        blank=True
    )

    description = models.TextField()
    xp = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)
    is_added = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_done and not self.done_at:
            self.done_at = datetime.datetime.now()

        if self.is_added is False and self.is_done is True:
            if self.outcome:
                self.outcome.total_xp += self.xp
                self.outcome.save()
            self.is_added = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.outcome} | {self.description} xp: {self.xp} is done: {self.is_done}'
