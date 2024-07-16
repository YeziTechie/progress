import datetime

from django.db import models


class TimeTask(models.Model):
    outcome = models.ForeignKey(
        'abilities.Outcome',
        models.SET_NULL,
        related_name='time_tasks',
        null=True,
        blank=True,
    )

    description = models.CharField(max_length=256)
    xp = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    longest_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_submit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.outcome} | {self.description} xp: {self.total_time * self.xp}'

    def save(self, *args, **kwargs):
        self.last_submit = datetime.datetime.now()
        super().save(*args, **kwargs)
