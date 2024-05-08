from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=100)
    total_xp = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_task_done_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} | XP: {self.total_xp}'

