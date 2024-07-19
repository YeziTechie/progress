from django.utils import timezone

from django.db import models


class Deadline(models.Model):

    penalty_choices = [
        (0.5, 'Half XP loose'),
        (1, 'Equal XP loose'),
        (2, 'Double XP loose'),
        (4, 'Four fold XP loose'),
    ]

    outcome = models.ForeignKey(
        'abilities.Outcome',
        models.SET_NULL,
        related_name='deadline_tasks',
        null=True,
        blank=True
    )

    description = models.CharField(max_length=512)
    xp = models.IntegerField(default=0)
    penalty_xp = models.IntegerField(default=0)
    report = models.CharField(max_length=1024, null=True, blank=True)
    penalty = models.IntegerField(choices=penalty_choices, default=1)
    deadline_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_aborted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description} (due {self.deadline_date})'

    def is_time_over(self):
        if self.deadline_date is None:
            return False
        return self.deadline_date < timezone.now()
