from django.db import models

from outcome import Outcome


class Questions(models.Model):
    outcome = models.OneToOneField(
        on_delete=models.CASCADE,
        to=Outcome,
        null=False
    )
    positive = models.CharField(max_length=128, default='Not answered yet.', null=True)
    evidence = models.CharField(max_length=1024, default='Not answered yet.', null=True)
    specific = models.CharField(max_length=256, default='Not answered yet.', null=True)
    resource = models.CharField(max_length=1024, default='Not answered yet.', null=True)
    control = models.CharField(max_length=256, default='Not answered yet.', null=True)
    identity = models.CharField(max_length=512, default='Not answered yet.', null=True)
    relation_with_other_outcomes = models.CharField(max_length=1028, default='Not answered yet.', null=True)
    action = models.CharField(max_length=512, default='Not answered yet.', null=True)
