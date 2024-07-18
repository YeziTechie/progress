from datetime import timedelta
from django.utils import timezone

from django.db import models


class Deadline(models.Model):

    penalty_choices = [
        ('Half', 'Half XP loose'),
        ('Equal', 'Equal XP loose'),
        ('Double', 'Double XP loose'),
        ('Fourfold', 'Four fold XP loose'),
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
    report = models.CharField(max_length=1024, null=True)
    penalty = models.CharField(choices=penalty_choices, max_length=32)

    deadline_date = models.DateTimeField(null=True, blank=True)
    duration_days = models.IntegerField(null=True, blank=True)
    duration_hours = models.IntegerField(null=True, blank=True)

    is_done = models.BooleanField(default=False)
    is_aborted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.deadline_date and (self.duration_days or self.duration_hours):
            now = timezone.now()
            days = self.duration_days or 0
            hours = self.duration_hours or 0
            self.deadline_date = now + timedelta(days=days, hours=hours)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.description} (due {self.deadline_date})'

    def is_time_over(self):
        return self.deadline_date < timezone.now()
