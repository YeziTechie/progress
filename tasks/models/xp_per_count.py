from django.db import models
from abilities.models.outcome import Outcome
import datetime


class XpPerCountTask(models.Model):

    outcome = models.ForeignKey(
        Outcome,
        on_delete=models.SET_NULL,
        related_name='xp_per_count_task_outcome',
        null=True,
        blank=True
    )

    description = models.CharField(max_length=256)
    xp = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_submit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.outcome} | {self.description} xp: {self.total_count}'
