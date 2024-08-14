from django.db import models
import datetime


class Classic(models.Model):

    outcome = models.ForeignKey(
        'outcomes.Outcome',
        models.CASCADE,
        related_name='classic_tasks',
        null=False,
        blank=False
    )

    description = models.TextField(null=False, blank=False)
    report = models.CharField(max_length=1024, null=True, blank=True)
    xp = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_done and not self.done_at:
            self.done_at = datetime.datetime.now()

        if self.is_done:
            self.outcome.last_task_done_at = datetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.outcome} | {self.description} xp: {self.xp} is done: {self.is_done}'
