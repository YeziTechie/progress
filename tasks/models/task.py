from django.db import models
from abilities.models.ability import Ability
import datetime


class Task(models.Model):

    ability = models.ForeignKey(
        Ability,
        on_delete=models.SET_NULL,
        related_name='tasks_ability',
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
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ability} | {self.description} xp: {self.xp} is done: {self.is_done}'
